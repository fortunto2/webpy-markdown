# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import web
import markdown
# web.config.debug = False

# URLs: map everything to the page class
urls = (
    '/(.*)', 'page',
    '/contacts', 'Contacts',
    '/info', 'Info',
)

# Templates are found in the templates directory
render = web.template.render('templates')

# Markdown
md = markdown.Markdown(output_format='html5')


class page:

    def GET(self, url):
        # Handle index pages: path/ maps to path/index.txt
        if url == "" or url.endswith("/"):
            url += "index"

        # Each URL maps to the corresponding .md file in pages/
        page_file = 'pages/%s.md' % (url)

        # Try to open the text file, returning a 404 upon failure
        try:
            f = open(page_file, 'r')
        except IOError:
            return web.notfound()

        # Read the entire file, converting Markdown content to HTML
        content = f.read()
        content = md.convert(content)

        # Render the page.html template using the converted content
        return render.page(content)

class Contacts:

    def GET(self):

        page_file = 'pages/contacts.md' % (url)

        content = open(page_file, 'r').read()
        content = md.convert(content)

        return render.page(content)

class Info:

    def GET(self):

        page_file = 'pages/info.md' % (url)

        content = open(page_file, 'r').read()
        content = md.convert(content)

        return render.page(content)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
