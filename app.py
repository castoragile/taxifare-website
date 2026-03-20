import streamlit as st
import requests

'''
# TaxiFareModel front
'''

pickup_datetime = st.text_input('Date and time', value="2014-07-06 19:18:00")
pickup_longitude = st.text_input('Pickup longitude', value="-73.950655")
pickup_latitude =	st.text_input('Pickup latitude', value="40.783282")
dropoff_longitude =	st.text_input('Dropoff longitude', value="-73.984365")
dropoff_latitude =	st.text_input('Dropoff latitude', value="40.769802")
passenger_count =	st.text_input('Passenger_count', value="2")


service_url = 'https://taxifare-93895098164.europe-west1.run.app/predict'

if st.button('Get fare estimate'):
    if all([pickup_datetime, pickup_longitude, pickup_latitude,
            dropoff_longitude, dropoff_latitude, passenger_count]):
        params = {
            'pickup_datetime': pickup_datetime,
            'pickup_longitude': float(pickup_longitude),
            'pickup_latitude': float(pickup_latitude),
            'dropoff_longitude': float(dropoff_longitude),
            'dropoff_latitude': float(dropoff_latitude),
            'passenger_count': int(passenger_count)
        }

 #       try:
        st.write("Envoi de la requête vers :", service_url)
        r = requests.get(service_url, params=params, timeout=5)
        response = r.json()
        #st.write("Réponse reçue, status :", r.status_code)
        #st.write("Réponse brute :", r.text)
        st.markdown(f"### Expected fare is: {round(response['fare'], 2)}")

#        except requests.exceptions.Timeout:
#            st.error("⏱️ Timeout : aucune réponse après 5s")
#        except requests.exceptions.ConnectionError as e:
#            st.error(f"🔌 Erreur de connexion : {e}")
#        except Exception as e:
#            st.error(f"❌ Erreur : {type(e).__name__} — {e}")



    else:
        st.warning("Please fill in all fields.")
