from ftw.testbrowser import browsing

from ftw.logo.tests import FunctionalTestCase


class TestAction(FunctionalTestCase):

    @browsing
    def test_action(self, browser):
        self.grant("Site Administrator")  # See "rolemap.xml".
        browser.login().visit(self.portal)
        self.assertEqual(
            "http://nohost/plone/logo-and-icon-overrides",
            browser.find("Override Site Logos").attrib["href"],
        )
