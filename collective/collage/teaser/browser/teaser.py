from Products.Collage.browser.views import BaseView

from collective.collage.teaser import teaserMessageFactory as _

class TeaserView(BaseView):
    title = _(u'Teaser')