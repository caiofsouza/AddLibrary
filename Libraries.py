import json
import sublime

try:
	from urllib.request import urlopen, Request
	from urllib.error import URLError
	from urllib.parse import urlencode
except ImportError:
	from urllib2 import urlopen, URLError
	from urllib2.parse import urlencode

class Libraries():

	def __init__(self):
		# lib_json = open(sublime.packages_path() + '/AddLibrary/Libraries.json')
		self.libraries = json.loads(sublime.load_resource("Packages/AddLibrary/Libraries.json"))

	def getLibrariesName(self):
		r = []
		for l in self.libraries:
			r.append(l['name'])

		return r

	def getLibraryByName(self, lib_name):
		r = ''
		for lib in self.libraries:
			if lib['name'] == lib_name:
				r = lib

		return r 

	def getLibraryBySearchName(self, lib_name):
		r = ''
		for lib in self.libraries:
			if lib['search_name'] == lib_name:
				r = lib

		return r 

	def getFileNameByLib(self, lib_name):
		r = ''
		for lib in self.libraries:
			if lib['name'] == lib_name:
				r = lib['file_name']

		return r 

	def httpGet(self, url):
		request_obj = Request(url, method='GET')
		req = urlopen(url=request_obj)
		return req
