# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema

from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable

from collective.z3cform.aceeditorwidget import AceEditorFieldWidget

from collective.advancedpage import _


class ILayer(Interface):
    pass


class IAdvancedPage(form.Schema, IImageScaleTraversable):
    """
    An advanced page with some goodies
    """

    form.primary('body')
    form.widget(body=AceEditorFieldWidget)
    body = schema.Text(
        title=_(u"Body"),
        description=_(
            u"Fill in the body of the page. Supports TAL templating."
        ),
        required=True,
        default=u""
    )

    show_title = schema.Bool(
        title=_(u'Show title?'),
        default=False,
    )

    show_description = schema.Bool(
        title=_(u'Show description?'),
        default=False,
    )

    include_hidden_structure = schema.Bool(
        title=_(u'Include hidden structure?'),
        description=_(u'This will render title and description '
                      u'for SEO even if not showing them.'),
        default=False,
    )
