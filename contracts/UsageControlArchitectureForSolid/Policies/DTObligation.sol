// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;
import "../Indexing/DTIndexing.sol";
import "../Libraries/Ownable.sol";

contract DTObligations is Ownable
{
    DTIndexing private dtIndexing;
    ObligationRules private defaultPodObligation;
    mapping(int=>ObligationRules) resourcesObligation;
    modifier hasSpecificRules(int resourceId)
    {
        require(withSpecificRules(resourceId),"The resource has not specific obligaitons rules. Add specific rules, or changhe the default pod rules.");
        _;
    }

    constructor(address dtInd,address podAddress){
        dtIndexing=DTIndexing(dtInd);
        transferOwnership(podAddress);

        }

        modifier isValidDeadline(int resourceId,uint deadline){
            ObligationRules memory obligations=getObligationRules(resourceId);
            require(!obligations.temporalObligation.exists,"A temporal obligation already exists for the resource");
            uint d=1 days;
            require(deadline>=block.timestamp+d,"The deadline is not valid");
            _;
        }
        modifier isValidTemporal(uint deadline)
        {
            uint d=1 days;
            require(deadline>d,"The temporal obligation must be at least 1 day");
            _;
        }


    modifier isTheResourceCovered(int idResource)
    {
        DTIndexing.Resource memory resource=dtIndexing.getResource(idResource);
        require(resource.owner==owner(),"The resource is not covered by this contract");
        _;
    }



    function getObligationRules(int idResource) isTheResourceCovered(idResource) public view returns(ObligationRules memory)
    {
        if (resourcesObligation[idResource].exists)
        {
            return resourcesObligation[idResource];
        }
        return defaultPodObligation;
    }
    function getDefaultObligationRules() public view returns(ObligationRules memory)
    {
        return defaultPodObligation;
    }





    function addDefaultAccessCounterObligation(uint accessCounter)public {
         defaultPodObligation.acObligation.exists=true;
         defaultPodObligation.acObligation.accessCounter=accessCounter;
    }
    function addDefaultTemporalObligation(uint temporalObligation)public isValidTemporal(temporalObligation) {
        uint d=1 days;
        require(temporalObligation>d,"The temporal obligation must be at least 1 day");
         defaultPodObligation.temporalObligation.exists=true;
         defaultPodObligation.temporalObligation.usageDuration=temporalObligation;
    }
    function addDefaultCountryObligation(uint country)public {
        defaultPodObligation.countryObligation.exists=true;
        defaultPodObligation.countryObligation.countryCode=country;
    }
    function adDefaultDomainObligation(DomainType domain) public
    {
        defaultPodObligation.domainObligation.exists=true;
        defaultPodObligation.domainObligation.domain=domain;
    }



    function addAccessCounterObligation(int idResource,uint accessCounter) isTheResourceCovered(idResource) public  returns(ObligationRules memory){
        if (resourcesObligation[idResource].exists){
            resourcesObligation[idResource].acObligation=AccessCounterObligation(accessCounter,true);
        }
        else{
                resourcesObligation[idResource].exists=true;
                resourcesObligation[idResource].idResource=idResource;
                resourcesObligation[idResource].acObligation=AccessCounterObligation(accessCounter,true);
        }
        return resourcesObligation[idResource];  
        }
    function addDomainObligation(int idResource,DomainType domain) public isTheResourceCovered(idResource)  returns(ObligationRules memory){
            if (resourcesObligation[idResource].exists){
                resourcesObligation[idResource].domainObligation=DomainObligation(domain,true);
            }
            else{
                    resourcesObligation[idResource].exists=true;
                    resourcesObligation[idResource].idResource=idResource;
                    resourcesObligation[idResource].domainObligation=DomainObligation(domain,true);
            }
            return resourcesObligation[idResource];  
    }
    function addCountryObligation(int idResource,uint country) public isTheResourceCovered(idResource)  returns(ObligationRules memory){
            if (resourcesObligation[idResource].exists){
                resourcesObligation[idResource].countryObligation=CountryObligation(country,true);
            }
            else{
                    resourcesObligation[idResource].exists=true;
                    resourcesObligation[idResource].idResource=idResource;
                    resourcesObligation[idResource].countryObligation=CountryObligation(country,true);
            }
            return resourcesObligation[idResource];  
    }
    function addTemporalObligation(int idResource,uint deadline) isTheResourceCovered(idResource) public isValidTemporal(deadline) returns(ObligationRules memory){

            if (resourcesObligation[idResource].exists){
                resourcesObligation[idResource].temporalObligation=TemporalObligation(deadline,true);
            }
            else{
                    resourcesObligation[idResource].exists=true;
                    resourcesObligation[idResource].idResource=idResource;
                    resourcesObligation[idResource].temporalObligation=TemporalObligation(deadline,true);
            }
            return resourcesObligation[idResource];  
    }







    function removeAccessCounterObligation(int idResource) isTheResourceCovered(idResource) public hasSpecificRules(idResource){

        resourcesObligation[idResource].acObligation.exists=false;
         resourcesObligation[idResource].acObligation.accessCounter=0;

    }
    function removeTemporalObligation(int idResource) isTheResourceCovered(idResource) public hasSpecificRules(idResource){

        resourcesObligation[idResource].temporalObligation.exists=false;
        resourcesObligation[idResource].temporalObligation.usageDuration=0;
    }
    function removeDomainObligation(int idResource) isTheResourceCovered(idResource) public hasSpecificRules(idResource){

        resourcesObligation[idResource].domainObligation.exists=false;
        resourcesObligation[idResource].domainObligation.domain=DomainType.NULL;
    }
     function removeCountryObligation(int idResource) isTheResourceCovered(idResource) public hasSpecificRules(idResource){

        resourcesObligation[idResource].countryObligation.exists=false;
        resourcesObligation[idResource].countryObligation.countryCode=0;
    }   







    function removeDefaultAccessCounterObligation() public {
        defaultPodObligation.acObligation.exists=false;
        defaultPodObligation.acObligation.accessCounter=0;
    }
    function removeDefaultTemporalObligation() public {
        
        defaultPodObligation.temporalObligation.exists=false;
        defaultPodObligation.temporalObligation.usageDuration=0;
    }
    function removeDefaultCountryObligation() public{
        defaultPodObligation.countryObligation.exists=false;
        defaultPodObligation.countryObligation.countryCode=0;
    }
    function removeDefaultDomainObligation() public{
        defaultPodObligation.domainObligation.exists=false;
        defaultPodObligation.domainObligation.domain=DomainType.NULL;
    }
    function withSpecificRules(int idResource)view public returns(bool)
    {
        return resourcesObligation[idResource].exists;
    }










struct ObligationRules{

    int idResource;
    AccessCounterObligation acObligation;
    CountryObligation countryObligation;
    TemporalObligation temporalObligation;
    DomainObligation domainObligation;
    bool exists;
}

struct AccessCounterObligation{

    uint accessCounter;
    bool exists;
}
struct CountryObligation{

    uint countryCode;
    bool exists;
}

struct TemporalObligation{

    uint usageDuration;
    bool exists;
}

struct DomainObligation{
    DomainType domain;
    bool exists;
}

enum DomainType{NULL,SOCIAL,FINANCIAL,MEDICAL}


}
