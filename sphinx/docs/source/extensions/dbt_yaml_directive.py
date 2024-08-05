import yaml
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging
import os

logger = logging.getLogger(__name__)

class DbtYamlDirective(SphinxDirective):
    has_content = True

    def run(self):
        if not self.content:
            return [self.state_machine.reporter.warning(
                'No YAML file specified', line=self.lineno)]

        yaml_file = self.content[0].strip()
        model_root_path = self.env.config.model_root_path
        model_toc_title = self.env.config.model_toc_title

        yaml_file_path = os.path.join(model_root_path, yaml_file)

        try:
            with open(yaml_file_path, 'r') as file:
                data = yaml.safe_load(file)
        except FileNotFoundError:
            return [self.state_machine.reporter.warning(
                f'File not found: {yaml_file_path}', line=self.lineno)]
        except yaml.YAMLError as exc:
            return [self.state_machine.reporter.warning(
                f'Error parsing YAML file: {exc}', line=self.lineno)]

        if 'models' not in data:
            return [self.state_machine.reporter.warning(
                'No models found in YAML file', line=self.lineno)]

        content = []

        # 目次を作成
        toc_section = nodes.section(ids=['model_toc'])
        toc_title = nodes.title(text=model_toc_title)
        toc_section += toc_title

        for model in data['models']:
            model_name = model['name']
            model_description = model['description']

            # 目次にリンクを追加
            toc_paragraph = nodes.paragraph()
            toc_paragraph += nodes.reference(text=model_name, refid=model_name)
            toc_paragraph += nodes.Text(f": {model_description}")
            toc_section += toc_paragraph

        content.append(toc_section)

        # 各モデルの詳細を追加
        for model in data['models']:
            content.extend(self.create_model_section(model))

        return content

    def create_model_section(self, model):
        model_name = model['name']
        model_description = model['description']
        columns = model['columns']

        section = nodes.section(ids=[model_name])
        title = nodes.title(text=model_name)
        section += title

        description = nodes.paragraph(text=model_description)
        section += description

        table = self.create_table(columns)
        section += table

        return [section]

    def create_table(self, columns):
        table = nodes.table()
        tgroup = nodes.tgroup(cols=3)
        table += tgroup

        tgroup += nodes.colspec(colwidth=1)
        tgroup += nodes.colspec(colwidth=1)
        tgroup += nodes.colspec(colwidth=2)

        thead = nodes.thead()
        tgroup += thead
        tbody = nodes.tbody()
        tgroup += tbody

        header_row = nodes.row()
        for header in ['Column Name', 'Type', 'Description']:
            entry = nodes.entry()
            entry += nodes.paragraph(text=header)
            header_row += entry
        thead += header_row

        for column in columns:
            row = nodes.row()
            for key in ['name', 'type', 'description']:
                entry = nodes.entry()
                entry += nodes.paragraph(text=column[key])
                row += entry
            tbody += row

        return table


def setup(app):
    app.add_config_value('model_root_path', '', 'env')
    app.add_config_value('model_toc_title', 'モデル一覧', 'env')
    app.add_directive("dbt_yaml", DbtYamlDirective)

