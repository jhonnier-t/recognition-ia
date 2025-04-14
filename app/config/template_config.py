import os

from jinja2 import Environment, FileSystemLoader

from app.config.exception_handler_config import ErrorHandler


def read_email_template(success, record_id, error_message="") -> str:
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(base_dir, "resources")
        env = Environment(loader=FileSystemLoader(template_path))
        template = env.get_template("template.html")
        rendered_html = template.render(success=success, record_id=record_id, error_message=error_message)
        return rendered_html
    except Exception as e:
        raise ErrorHandler.handle_general_error(e)

