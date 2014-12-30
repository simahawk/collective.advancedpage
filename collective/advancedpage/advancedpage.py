#-*- coding: utf-8 -*-

from Acquisition import aq_inner
from Acquisition import aq_base


from zope.component import getMultiAdapter
from zope.interface import implementer

from plone.dexterity.content import Container
from plone.outputfilters.interfaces import IFilter

from Products.Five.browser import BrowserView

from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate


from collective.advancedpage.interfaces import IAdvancedPage


@implementer(IAdvancedPage)
class AdvancedPage(Container):

    def body_compile(self):
        if not self.body:
            return ''
        pt = ZopePageTemplate(id='__adv_page_tal_body__')
        pt.pt_edit(self.body, 'text/html')
        context = aq_inner(self)
        pt = aq_base(pt).__of__(context)
        # request is taken by acquisition
        return pt()


class View(BrowserView):
    """AdvancedPage view class """

    def body(self):
        text = self.context.body_compile()
        # encode text before to resolve uids
        if isinstance(text, unicode):
            text = text.encode('utf-8')

        # trasform resolveuid link to absolute path
        _filter = getMultiAdapter(
            (self.context, self.request),
            IFilter, name="resolveuid_and_caption")
        try:
            text = _filter(text)
        except AttributeError:
            # Something wrong happend
            # perhaps image scale doesn't exists
            pass
        return text.decode('utf-8')

    def render_title(self):
        if self.context.show_title:
            return True
        return self.context.include_hidden_structure

    def render_description(self):
        if self.context.show_description:
            return True
        return self.context.include_hidden_structure

