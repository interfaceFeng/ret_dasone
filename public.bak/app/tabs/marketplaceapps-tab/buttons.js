/* -------------------------------------------------------------------------- */
/* Copyright 2002-2017, OpenNebula Project, OpenNebula Systems                */
/*                                                                            */
/* Licensed under the Apache License, Version 2.0 (the "License"); you may    */
/* not use this file except in compliance with the License. You may obtain    */
/* a copy of the License at                                                   */
/*                                                                            */
/* http://www.apache.org/licenses/LICENSE-2.0                                 */
/*                                                                            */
/* Unless required by applicable law or agreed to in writing, software        */
/* distributed under the License is distributed on an "AS IS" BASIS,          */
/* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   */
/* See the License for the specific language governing permissions and        */
/* limitations under the License.                                             */
/* -------------------------------------------------------------------------- */

define(function(require) {
  var Locale = require('utils/locale');

  var MarketPlaceAppButtons = {
    "MarketPlaceApp.refresh" : {
      type: "action",
      layout: "refresh",
      alwaysActive: true
    },
    "MarketPlaceApp.create_dialog" : {
      type: "create_dialog",
      layout: "create"
    },
    "MarketPlaceApp.download_opennebula_dialog" : {
      type: "action",
      text: '<i class="fa fa-share"/> '+ Locale.tr("OpenNebula")
    },
    "MarketPlaceApp.download_local" : {
      type: "action",
      text: '<i class="fa fa-lg fa-cloud-download"/>'
    },
    "MarketPlaceApp.chown" : {
      type: "confirm_with_select",
      text: Locale.tr("Change owner"),
      select: "User",
      layout: "user_select",
      tip: Locale.tr("Select the new owner")
    },
    "MarketPlaceApp.chgrp" : {
      type: "confirm_with_select",
      text: Locale.tr("Change group"),
      select: "Group",
      layout: "user_select",
      tip: Locale.tr("Select the new group")
    },
    "MarketPlaceApp.enable" : {
      type: "action",
      layout: "more_select",
      text: Locale.tr("Enable")
    },
    "MarketPlaceApp.disable" : {
      type: "action",
      layout: "more_select",
      text: Locale.tr("Disable")
    },
    "MarketPlaceApp.delete" : {
      type: "confirm",
      text: Locale.tr("Delete"),
      layout: "del"
    },
    "MarketPlaceApp.edit_labels" : {
      layout: "labels",
    }
  };

  return MarketPlaceAppButtons;
})
