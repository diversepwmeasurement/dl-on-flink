#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
from notification_service.master import NotificationMaster
from notification_service.service import NotificationService
from notification_service.event_storage import MemoryEventStorage


def start_notification_service(port: int = 50052):
    storage = MemoryEventStorage()
    notification_master \
        = NotificationMaster(service=NotificationService(storage), port=port)
    notification_master.run(is_block=True)


if __name__ == '__main__':
    start_notification_service()
