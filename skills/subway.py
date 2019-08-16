#  Copyright 2019 LINE Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


from linebot.models import LocationSendMessage

from skills import add_skill


@add_skill(r'지하철')
def get_location(message):
    return LocationSendMessage(
        title='지하철',
        subway='2호선 삼성역 5번출구, 9호선 봉은사역 7번출구, 7호선 청담역 2번 출구'
    )
