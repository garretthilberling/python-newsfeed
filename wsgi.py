import os
from app import app as application

port = int(os.environ.get("PORT", 5000))
application.run(debug=True, host='0.0.0.0', port=port)