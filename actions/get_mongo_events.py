# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction


class loadDb(MongoBaseAction):
    def run(self):

        mydb = self.dbclient["app_db"]
        known = mydb["nimbleevents"]

        list_to_process = []

        myquery = { "u_process" : 'no' }
        records = known.find(myquery)

        for r in records:
            # Do not update. Keep the code for reference
            # known.update_one({"_id":r['_id']},{"$set":{"u_process":"yes"}})
            # known.delete_one("_id" : r['_id'])
            list_to_process.append(r)


        return (list_to_process)
