# zope imports
from zope import schema
from zope.formlib import form
from zope.interface import implements

# plone imports
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider


class INewsletterSubscriberPortlet(IPortletDataProvider):
    """
    """
    portlet_title = schema.TextLine(
        title = _(u"Title for the portlet."),
        default = u"Newsletter",
        required = True,
    )

    portlet_description = schema.Text(
            title=_(u"label_newsletter_description", default=u"Description"),
            description=_(u"help_newsletter_description",
                          default=u"Subscribe here to our newsletter."),
            default=u"",
            required=False)

    newsletter = schema.TextLine(
            title=_(u"label_newsletter_title", default=u"Path to Newsletter"),
            description=_(u"help_newsletter_title",
                          default=u"The absolute path from portal_root to the newsletter"),
            default=u"",
            required=True)


class Assignment(base.Assignment):
    """
    """
    implements(INewsletterSubscriberPortlet)

    def __init__(self, portlet_title="", portlet_description="", newsletter=""):
        """
        """
        self.portlet_title = portlet_title
        self.portlet_description = portlet_description
        self.newsletter = newsletter

    @property
    def title(self):
        """
        """
        return _(u"Newsletter Subscriber")

class Renderer(base.Renderer):
    """
    """
    render = ViewPageTemplateFile('subscriber.pt')

    @property
    def available(self):
        """
        """
        return True

    def header(self):
        return self.data.portlet_title

    def description(self):
        return self.data.portlet_description

    def get_newsletter(self):
        """
        """
        return self.data.newsletter

class AddForm(base.AddForm):
    """
    """
    form_fields = form.Fields(INewsletterSubscriberPortlet)
    def create(self, data):
        """
        """
        return Assignment(
            portlet_title = data.get("portlet_title", ""),
            portlet_description = data.get("portlet_description", ""),
            newsletter = data.get("newsletter", ""),
        )

class EditForm(base.EditForm):
    """
    """
    form_fields = form.Fields(INewsletterSubscriberPortlet)
    label = _(u"Edit Newsletter portlet")
    description = _(u"This portlet displays the subscriber add form of a newsletter.")





