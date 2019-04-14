# -*- coding: utf-8 -*- #
# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The super-group for the IAP web CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Web(base.Group):
  """Manage IAP web policies.

     Cloud Identity-Aware Proxy (Cloud IAP) controls access to your cloud
     applications running on Google Cloud Platform. Cloud IAP works by
     verifying user identity and context of the request to determine if a user
     should be allowed to access the application.

     More information on Cloud IAP can be found here:
     https://cloud.google.com/iap and detailed documentation can be found here:
     https://cloud.google.com/iap/docs/
  """

  category = 'Identity and Security'
