from google.appengine.ext import vendor
import os

vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))
