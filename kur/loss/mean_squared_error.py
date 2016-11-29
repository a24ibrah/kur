"""
Copyright 2016 Deepgram

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from . import Loss

################################################################################
class MeanSquaredError(Loss):
	""" Mean squared error: a simple loss function to minimize distance between
		the model output and the true value.
	"""

	############################################################################
	@classmethod
	def get_name(cls):
		""" Returns the name of the loss function.
		"""
		return 'mean_squared_error'

	############################################################################
	def get_loss(self, backend):

		if backend.get_name() == 'keras':
			return 'mean_squared_error'
		else:
			raise ValueError('Unsupported backend "{}" for loss function "{}"'
				.format(backend.get_name(), self.get_name()))

#### EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF.EOF
