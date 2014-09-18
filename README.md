ODS-KSK-rollover-OVH
====================

Little bash script to automatically sync the KSK rollover in OVH console panel

* Change your NIC-Handle, Password, and domains you want to keep in sync
  save the variable to the .config file

* update your kasp.xml config file with 
  <Enforcer>
     [...]
     <RolloverNotification>P14D</RolloverNotification>  <!-- get notification 14D about the rollover --!>
     <DelegationSignerSubmitCommand>/PATH/TO/SCRIPT/opendnssec-updateDS</DelegationSignerSubmitCommand>
  </Enforcer>


TODO:
 * timeout on ods-ksmutil in case on lock 
   + specially on crontab
 * put a lock on the crontab to disable execute in case of process already started
