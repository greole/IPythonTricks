from IPython.display import HTML

class NotebookObject():

    def __init__(self, code_block):
        self.code_block = code_block


    def _repr_html_(self):
        return self.code_block

ToggleCodeButton = NotebookObject('''<script>
code_show=false;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')

EnableEquationNumbers = NotebookObject(""" <script type="text/Javascript"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "AMS", useLabelIds: true } }});
</script>""")

class DictTable(dict):
    # Overridden dict class which takes a dict in the form {'a': 2, 'b': 3},
    # and renders an HTML Table in IPython Notebook.
    def __getattr__(self, item):
        return self[item]

    def _repr_html_(self):
        html = ["<table width=100%>"]
        for key, value in self.iteritems():
            html.append("<tr>")
            html.append("<td>{0}</td>".format(key))
            html.append("<td>{0}</td>".format(value))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)

class DictValueTable(dict):
    # Overridden dict class which takes a dict in the form {'a': {'val':'foo',
    #                                                             'label':'foo [b]'
    #                                                        },
    # and renders an HTML Table in IPython Notebook.
    def __getattr__(self, item):
        return self[item]['val']

    def set(self, item, value):
        d = {item: value for item, value in self.iteritems()}
        d[item]['val'] = value
        return DictValueTable(d)

    def _repr_html_(self):
        html = ["<table width=100%>"]
        for key, subdict in self.iteritems():
            dis = subdict['label']
            val = subdict['val']
            html.append("<tr>")
            html.append("<td>{0}</td>".format(dis))
            html.append("<td>{0}</td>".format(val))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
