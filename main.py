import os
from app import app

if __name__ == "__main__":
    # Render assigns PORT dynamically – fallback must NOT be 5000
    port = int(os.environ.get("PORT", 10000))

    # Disable debug for production
    debug_mode = os.environ.get('FLASK_ENV') == 'development'

    app.run(host="0.0.0.0", port=port, debug=debug_mode, use_reloader=False)
