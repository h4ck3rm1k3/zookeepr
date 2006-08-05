from zookeepr.lib.base import *

class RegisterController(BaseController):

    def confirm(self, id):
        """Confirm a registration with the given ID.

        `id` is a md5 hash of the email address of the registrant, the time
        they regsitered, and a nonce.

        """
        r = self.objectstore.query(model.Registration).select_by(_url_hash=id)

        if len(r) < 1:
            abort(404)

        r[0].activated = True

        self.objectstore.save(r[0])
        self.objectstore.flush()

        return render_response('register/confirmed.myt')
