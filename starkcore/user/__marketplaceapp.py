from .__user import User


class MarketplaceApp(User):
    """
    #MarketplaceApp object
    The MarketplaceApp object is an authentication entity for the SDK that
    represents your entire MarketplaceApp, being able to access any Workspace
    underneath it and even create new Workspaces. Only a legal representative
    of your MarketplaceApp can register or change the MarketplaceApp credentials.
    All requests to the Stark Bank API must be authenticated via an SDK user,
    which must have been previously created at the Stark Bank website
    [https://web.sandbox.starkbank.com] or [https://web.starkbank.com]
    before you can use it in this SDK. MarketplaceApps may be passed as the user parameter on
    each request or may be defined as the default user at the start (See README).
    If you are accessing a specific Workspace using MarketplaceApp credentials, you should
    specify the workspace ID when building the MarketplaceApp object or by request, using
    the MarketplaceApp.set_workspace(workspace_id) method, which creates a copy of the MarketplaceApp
    object with the altered workspace ID. If you are listing or creating new Workspaces, the
    workspace_id should be null.
    ## Parameters (required):
    - environment [string]: environment where the MarketplaceApp is being used. ex: "sandbox" or "production"
    - id [string]: unique id required to identify MarketplaceApp. ex: "5656565656565656"
    - privateKey [EllipticCurve.MarketplaceApp()]: PEM string of the private key linked to the MarketplaceApp. ex: "-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEyTIHK6jYuik6ktM9FIF3yCEYzpLjO5X/\ntqDioGM+R2RyW0QEo+1DG8BrUf4UXHSvCjtQ0yLppygz23z0yPZYfw==\n-----END PUBLIC KEY-----"
    - authorizationId [string]: unique id of the accessed Workspace, if any. ex: null or "4848484848484848"
    ## Attributes (return-only):
    -
    """

    def __init__(
        self,
        id,
        environment,
        private_key,
        authorization_id=None,
    ):
        self.authorization_id = authorization_id

        User.__init__(
            self,
            id=id,
            private_key=private_key,
            environment=environment,
        )

    def access_id(self):
        if self.authorization_id != None:
            return "marketplace-app-authorization/" + self.authorization_id
        return "marketplace-app/{id}".format(id=self.id)

    def replace(marketplace_app, authorization_id):
        return MarketplaceApp(
            environment=marketplace_app.environment,
            id=marketplace_app.id,
            private_key=marketplace_app.pem,
            authorization_id=authorization_id,
        )
