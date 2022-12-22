from config import app
import views
from user import views
if __name__ == "__main__":
    app.run(debug=True,port=9999)