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


from linebot.models import LunchSendMessage

from skills import add_skill

import random
foods = ['자장면', '짬뽕', '탕수육', '잡채', '떡볶이', '라면', '한식', '돈가스', '김밥', '국수', '김치찌개', '된장찌개', '구내식당', '피자', '햄버거', '비빔밥', '불고기', '삼겹살', '치킨', '갈비', '생선구이', '냉면', '국밥', '삼계탕', '순두부찌개', '파전', '죽']
food = random.choice(foods)
presenter.remove(food)

@add_skill(r'점심')
def get_lunch(message):
    return LunchSendMessage(
        title='점심',
        lunch=food
    )
