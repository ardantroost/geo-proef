from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy_garden.mapview import MapView,MapMarker,MapMarkerPopup
from geopy import distance

class GeodisplayScreen(Screen):

	def compute_distance(self, lat1, lon1, lat2, lon2):
		a=(lat1,lon1)
		b=(lat2,lon2)
		#bereken (en rond af) de afstand in meters tussen de twee coordinaten
		self.socialdistance = (distance.distance(a,b).m)
		mtrs="{:.2f}". format(self.socialdistance)
		self.ids._distance.text=(str(mtrs))+" meters"
		# print coord-bounderies of map (linksboven, rechtsonder)
		print(self.ids._geoview.bbox)

	def update_makers(self,lon,lat):

		map_marker = MapMarkerPopup(lat=lat, lon=lon)
		self.ids._geoview.add_marker(map_marker)
		self.ids._geoview.add_marker(MapMarkerPopup(lon=lon, lat=lat))

		#self.ids._pop.lat=lat
		#self.ids._pop.lon = lon

	def display_info_marker(self):

		def on_release():
			bubble = Bubble(orientation='vertical', background_image="home.png")
			map_marker = MapMarkerPopup(lat=52.091138,lon=5.244849)
			map_marker.add_widget(bubble)
			self.ids._geoview.add_marker(map_marker)
