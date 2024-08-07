import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st;
import json

key_dict = json.loads(st.secrets['textkey'])

# Fetch the service account key JSON file contents
creds = service_account.Credentials.from_service_account_info(key_dict)

# Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://tiramisucake-b5e42-default-rtdb.firebaseio.com/'
# })

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('test/value')
quiz = ref.child('quiz')
quiz.set({
    "name":st.session_state.name,
    "score":st.session_state.score
})
