import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    # DISABLED DEBUG MODE - was causing repeated app restarts during deployment
    # Use debug=False for production/deployment to prevent auto-reloader from restarting app
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(host="0.0.0.0", port=port, debug=debug_mode, use_reloader=False)
