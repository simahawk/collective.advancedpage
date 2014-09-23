#-*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema

from plone.directives import form
from plone.namedfile.interfaces import IImageScaleTraversable

from collective.advancedpage import _


class ILayer(Interface):
    pass


class IAdvancedPage(form.Schema, IImageScaleTraversable):
    """
    An advanced page with some goodies
    """

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
