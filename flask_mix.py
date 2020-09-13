import json
import os

from flask import current_app


class Mix:
    """
    Mix extends a Flask app by adding a `mix` template helper for including 
    static files managed by Laravel Mix.

    See https://laravel-mix.com for more information on Laravel Mix.
    """

    def __init__(self, app=None):
        self.app = app
        self.assets = ''
        self.assets_url = ''

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initializes the extension. The assets and optional asset URL are loaded
        from disk when the app starts. In debug mode, the assets and asset url
        are reloaded from disk before each request.
        """
        app.config.setdefault('MIX_ASSETS_BASE_URL', '')
        app.config.setdefault('MIX_MANIFEST_PATH',
                              os.path.join(app.static_folder,
                                           'mix-manifest.json'))
        app.config.setdefault('MIX_HOT_PATH',
                              os.path.join(app.static_folder, 'hot'))
        
        self.get_assets(app)
        self.get_assets_base_url(app)

        if app.config.get('DEBUG'):
            app.before_request(self.reload)

        app.add_template_global(self.mix)

    def reload(self):
        """
        Reloads the assets and assets URL from disk. Should only be used in
        DEBUG mode.
        """
        self.get_assets(current_app)
        self.get_assets_base_url(current_app)

    def get_assets(self, app):
        """
        Loads the asset map from the mix manifest file on disk.
        """
        manifest_path = app.config.get('MIX_MANIFEST_PATH')

        try:
            with app.open_resource(manifest_path, 'r') as manifest:
                self.assets = json.load(manifest)
        except IOError:
            raise RuntimeError(
                "MIX_MANIFEST_PATH requires a valid mix-manifest.json file"
            )

    def get_assets_base_url(self, app):
        """
        Loads the assets url from the mix hot file on disk or from the
        MIX_ASSETS_BASE_URL environment variable.
        """
        hot_path = app.config.get('MIX_HOT_PATH')

        try:
            with app.open_resource(hot_path, 'r') as hot_file:
                base_url = hot_file.read().strip()
                if base_url.endswith('/'):
                    base_url = base_url[:-1]
                self.assets_base_url = base_url
        except:
            self.assets_base_url = app.config.get('MIX_ASSETS_BASE_URL')
    
    def mix(self, file):
        """
        Method exposed to templates that can be given the path to a source
        asset and will return the path to built static asset.
        """
        if not self.assets:
            return ''

        return self.assets_base_url + self.assets.get(file)
