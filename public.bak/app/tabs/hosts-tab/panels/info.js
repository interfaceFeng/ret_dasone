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
  /*
    DEPENDENCIES
   */
  require('foundation');
  var Locale = require('utils/locale');
  var Humanize = require('utils/humanize');
  var RenameTr = require('utils/panel/rename-tr');
  var TemplateTable = require('utils/panel/template-table');
  var TemplateTableVcenter = require('utils/panel/template-table');
  var PermissionsTable = require('utils/panel/permissions-table');
  var ClusterTr = require('utils/panel/cluster-tr');
  var OpenNebulaHost = require('opennebula/host');
  var CPUBars = require('../utils/cpu-bars');
  var MemoryBars = require('../utils/memory-bars');
  var DatastoresCapacityTable = require('../utils/datastores-capacity-table');
  var CanImportWilds = require('../utils/can-import-wilds');
  var Sunstone = require('sunstone');
  var TemplateUtils = require('utils/template-utils');
  var CapacityTable = require('utils/custom-tags-table');
  var EC2Tr = require('utils/panel/ec2-tr');

  /*
    TEMPLATES
   */

  var TemplateInfo = require('hbs!./info/html');

  /*
    CONSTANTS
   */

  var TAB_ID = require('../tabId');
  var PANEL_ID = require('./info/panelId');
  var RESOURCE = "Host";
  var XML_ROOT = "HOST";

  var OVERCOMMIT_DIALOG_ID = require('utils/dialogs/overcommit/dialogId');

  /*
    CONSTRUCTOR
   */

  function Panel(info) {
    var that = this;
    that.title = Locale.tr("Info");
    that.icon = "fa-info-circle";

    that.element = info[XML_ROOT];
    that.canImportWilds = CanImportWilds(that.element);

    // Hide information of the Wild VMs of the Host and the ESX Hosts
    //  in the template table. Unshow values are stored in the unshownTemplate
    //  object to be used when the host info is updated.
    that.unshownTemplate = {};
    that.strippedTemplateVcenter = {};
    that.strippedTemplate = {};
    var unshownKeys = ['HOST', 'VM', 'WILDS', 'ZOMBIES', 'RESERVED_CPU', 'RESERVED_MEM', "EC2_ACCESS", "EC2_SECRET", "CAPACITY", "REGION_NAME"];
    $.each(that.element.TEMPLATE, function(key, value) {
      if ($.inArray(key, unshownKeys) > -1) {
       that.unshownTemplate[key] = value;
      }
      else if (!key.match(/^VCENTER_RESOURCE_POOL$/) && key.match(/^VCENTER_*/)){
        that.strippedTemplateVcenter[key] = value;
      }
      else {
        that.strippedTemplate[key] = value;
      }
    });

    return this;
  };

  Panel.PANEL_ID = PANEL_ID;
  Panel.prototype.html = _html;
  Panel.prototype.setup = _setup;

  return Panel;

  /*
    FUNCTION DEFINITIONS
   */
  function _html() {
    var templateTableHTML = TemplateTable.html(
                                      this.strippedTemplate,
                                      RESOURCE,
                                      Locale.tr("Attributes"));
    var templateTableVcenterHTML = TemplateTableVcenter.html(
                                      this.strippedTemplateVcenter,
                                      RESOURCE,
                                      Locale.tr("vCenter information"),false);
    var renameTrHTML = RenameTr.html(TAB_ID, RESOURCE, this.element.NAME);
    var clusterTrHTML = ClusterTr.html(this.element.CLUSTER);
    var permissionsTableHTML = PermissionsTable.html(TAB_ID, RESOURCE, this.element);
    var cpuBars = CPUBars.html(this.element);
    var memoryBars = MemoryBars.html(this.element);
    var datastoresCapacityTableHTML = DatastoresCapacityTable.html(this.element);
    var realCPU = parseInt(this.element.HOST_SHARE.TOTAL_CPU);
    var realMEM = parseInt(this.element.HOST_SHARE.TOTAL_MEM);

    return TemplateInfo({
      'element': this.element,
      'renameTrHTML': renameTrHTML,
      'clusterTrHTML': clusterTrHTML,
      'templateTableHTML': templateTableHTML,
      'templateTableVcenterHTML': templateTableVcenterHTML,
      'permissionsTableHTML': permissionsTableHTML,
      'cpuBars': cpuBars,
      'memoryBars': memoryBars,
      'stateStr': OpenNebulaHost.stateStr(this.element.STATE),
      'datastoresCapacityTableHTML': datastoresCapacityTableHTML,
      'maxReservedMEM': realMEM * 2,
      'maxReservedCPU': realCPU * 2,
      'realCPU': realCPU,
      'realMEM': Humanize.size(realMEM),
      'virtualMEMInput': Humanize.size(this.element.HOST_SHARE.MAX_MEM),
      'ec2_tr': EC2Tr.html(RESOURCE, this.element.TEMPLATE),
      'capacityTableHTML': CapacityTable.html()
    });
  }

   function changeInputCPU(maxCPU){
    document.getElementById('change_bar_cpu_hosts').value = parseInt(document.getElementById('textInput_reserved_cpu_hosts').value);
    document.getElementById('textInput_reserved_cpu_hosts').value = document.getElementById('change_bar_cpu_hosts').value;
    changeColorInputCPU(maxCPU);
  }

   function changeInputMEM(maxMEM){
    document.getElementById('change_bar_mem_hosts').value = Humanize.sizeToMB(document.getElementById('textInput_reserved_mem_hosts').value);
    document.getElementById('textInput_reserved_mem_hosts').value = Humanize.size(document.getElementById('change_bar_mem_hosts').value);
    changeColorInputMEM(maxMEM);
  }

  function changeColorInputCPU(maxCPU){
    if(parseInt(document.getElementById('change_bar_cpu_hosts').value) > parseInt(maxCPU)){
      document.getElementById('textInput_reserved_cpu_hosts').style.backgroundColor = 'rgba(111, 220, 111, 0.5)';
    }
    else if(parseInt(document.getElementById('change_bar_cpu_hosts').value) < parseInt(maxCPU)){
      document.getElementById('textInput_reserved_cpu_hosts').style.backgroundColor = 'rgba(255, 80, 80, 0.5)';
    } else {
      document.getElementById('textInput_reserved_cpu_hosts').style.backgroundColor = 'white';
    }
  }

  function changeColorInputMEM(maxMEM){
    if(parseInt(document.getElementById('change_bar_mem_hosts').value) > parseInt(maxMEM)){
      document.getElementById('textInput_reserved_mem_hosts').style.backgroundColor = 'rgba(111, 220, 111, 0.5)';
    }
    else if(parseInt(document.getElementById('change_bar_mem_hosts').value) < parseInt(maxMEM)){
      document.getElementById('textInput_reserved_mem_hosts').style.backgroundColor = 'rgba(255, 80, 80, 0.5)';
    } else {
      document.getElementById('textInput_reserved_mem_hosts').style.backgroundColor = 'white';
    }
  }

  function _setup(context) {
    var that = this;
    $(".ec2",context).show();
    RenameTr.setup(TAB_ID, RESOURCE, this.element.ID, context);
    ClusterTr.setup(RESOURCE, this.element.ID, this.element.CLUSTER_ID, context);

    TemplateTable.setup(this.strippedTemplate, RESOURCE, this.element.ID, context, this.unshownTemplate, this.strippedTemplateVcenter);
    TemplateTableVcenter.setup(this.strippedTemplateVcenter, RESOURCE, this.element.ID, context, this.unshownTemplate, this.strippedTemplate);

    PermissionsTable.setup(TAB_ID, RESOURCE, this.element, context);

    if($.isEmptyObject(this.strippedTemplateVcenter)){
      $('.vcenter', context).hide();
    }

    //.off and .on prevent multiple clicks events
    $(document).off('click', '.update_reserved_hosts').on("click", '.update_reserved', function(){
        var reservedCPU = parseInt(document.getElementById('change_bar_cpu_hosts').value);
        var CPU = parseInt(that.element.HOST_SHARE.FREE_CPU);
        var reservedMem = parseInt(document.getElementById('change_bar_mem_hosts').value);
        var MEM = parseInt(that.element.HOST_SHARE.FREE_MEM);
        if(parseInt(that.element.HOST_SHARE.USED_CPU) > 0)
          CPU += parseInt(that.element.HOST_SHARE.USED_CPU);
        reservedCPU = CPU - reservedCPU;
        if(parseInt(that.element.HOST_SHARE.USED_MEM) > 0)
          MEM += parseInt(that.element.HOST_SHARE.USED_MEM);
        reservedMem = MEM - reservedMem;

        var obj = {RESERVED_CPU: reservedCPU, RESERVED_MEM: reservedMem};
        Sunstone.runAction("Host.append_template", that.element.ID, TemplateUtils.templateToString(obj));
    });

    document.getElementById("change_bar_cpu_hosts").addEventListener("input", function(){
      changeColorInputCPU(that.element.HOST_SHARE.TOTAL_CPU);
      document.getElementById('textInput_reserved_cpu_hosts').value = document.getElementById('change_bar_cpu_hosts').value;
    });
    document.getElementById("textInput_reserved_cpu_hosts").addEventListener("input", function(){
      changeInputCPU(that.element.HOST_SHARE.TOTAL_CPU);
    });
    document.getElementById("change_bar_mem_hosts").addEventListener("input", function(){
      changeColorInputMEM(that.element.HOST_SHARE.TOTAL_MEM);
      document.getElementById('textInput_reserved_mem_hosts').value = Humanize.size(parseInt(document.getElementById('change_bar_mem_hosts').value));
    });

    document.getElementById("textInput_reserved_mem_hosts").addEventListener("input", function(){
      changeInputMEM(that.element.HOST_SHARE.TOTAL_MEM);
    });

    CapacityTable.setup(context, true, RESOURCE, this.element.TEMPLATE, this.element.ID);
    EC2Tr.setup(RESOURCE, this.element.ID, context);
    CapacityTable.fill(context, this.element.TEMPLATE.CAPACITY);
    $(".change_to_vector_attribute", context).hide();
    $(".custom_tag_value",context).focusout(function(){
        var key = $(".custom_tag_key",this.parentElement.parentElement).val();
        if(!that.element.TEMPLATE.CAPACITY){
          that.element.TEMPLATE.CAPACITY = {};
        }
        that.element.TEMPLATE.CAPACITY[key] = this.value;
        Sunstone.runAction(RESOURCE+".update_template",that.element.ID, TemplateUtils.templateToString(that.element.TEMPLATE));
      });
    if (this.element.TEMPLATE.IM_MAD != "ec2"){
      $(".ec2",context).hide();
    }
  }
});
