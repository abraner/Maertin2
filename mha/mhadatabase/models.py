from phone_field import PhoneField
from django.db import models
from decimal import Decimal
from django.core.exceptions import ValidationError

class ContractorInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, unique=True, verbose_name="Con. ID.")
    concompanytname = models.CharField(max_length=50, blank=True, verbose_name="Company Name:")
    confirstname = models.CharField(max_length=45, verbose_name="First Name:")
    conlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    conadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    conadd2 = models.CharField(max_length=45, blank=True, verbose_name="Address #2:")
    concity = models.CharField(max_length=45, verbose_name="City:")
    const = models.CharField(max_length=15, verbose_name="St:")
    conzipcode = models.CharField(max_length=15, verbose_name="Zip Code:")
    conwork1 = PhoneField(blank=True, verbose_name="Work Phone #1:")
    conwork2 = PhoneField(blank=True, verbose_name="Work Phone #2:")
    concell1 = PhoneField(blank=True, verbose_name="Cell Phone #1:")
    concell2 = PhoneField(blank=True, verbose_name="Cell Phone #2:")
    conhome = PhoneField(blank=True, verbose_name="Home Phone:")
    conemail1 = models.EmailField(max_length=254, blank=True, verbose_name="Email #1:")
    conemail2 = models.EmailField(max_length=254, blank=True, verbose_name="Email #2:")

    class Meta:
        unique_together = ["confirstname", "conlastname", "conadd1", "concity", "const"]


    def get_absolute2_url(self):
        return f"/mhadatabase/{self.id}/contractorpage/"

    def get_absolute3_url(self):
        return f"/mhadatabase/{self.id}/addcust"

    def get_absolute8_url(self):
        return f"/mhadatabase/{self.id}/addcustconfirm/"

    def get_absolute14_url(self):
        return f"/mhadatabase/{self.custid}/newcust"

    def get_absolute16_url(self):
        return f"/mhadatabase/{self.id}/jobselection"



class ContractorSearch(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    concompanytname = models.CharField(null=True,max_length=50, blank=True, verbose_name="Company Name:")
    confirstname = models.CharField(null=True,max_length=45, blank=True, verbose_name="First Name:")
    conlastname = models.CharField(null=True,max_length=45, blank=True, verbose_name="Last Name:")
    conadd1 = models.CharField(null=True,max_length=45, blank=True, verbose_name="Address #1:")
    concity = models.CharField(null=True,max_length=45, blank=True, verbose_name="City:")
    custcompanytname = models.CharField(null=True, max_length=50, blank=True, verbose_name="Company Name:")
    custfirstname = models.CharField(null=True, max_length=45, blank=True, verbose_name="First Name:")
    custlastname = models.CharField(null=True, max_length=45, blank=True, verbose_name="Last Name:")
    custadd1 = models.CharField(null=True, max_length=45, blank=True, verbose_name="Address #1:")
    custcity = models.CharField(null=True, max_length=45, blank=True, verbose_name="City:")




class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="Con ID.")
    custcompanytname = models.CharField(null=True, max_length=50, blank=True, verbose_name="Company Name:")
    custfirstname = models.CharField(null=True, max_length=45, verbose_name="First Name:")
    custlastname = models.CharField(null=True, max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(null=True, max_length=45, verbose_name="Address #1:")
    custadd2 = models.CharField(null=True, max_length=45, blank=True, verbose_name="Address #2:")
    custcity = models.CharField(null=True, max_length=45, verbose_name="City:")
    custst = models.CharField(null=True, max_length=15, verbose_name="St:")
    custzipcode = models.CharField(null=True, max_length=15, verbose_name="Zip Code:")
    custwork1 = PhoneField(null=True, blank=True, verbose_name="Work Phone #1:")
    custwork2 = PhoneField(null=True, blank=True, verbose_name="Work Phone #2:")
    custcell1 = PhoneField(null=True, blank=True, verbose_name="Cell Phone #1:")
    custcell2 = PhoneField(null=True, blank=True, verbose_name="Cell Phone #2:")
    custhome = PhoneField(null=True, blank=True, verbose_name="Home Phone:")
    custemail1 = models.EmailField(max_length=254,null=True, blank=True, verbose_name="Email #1:")
    custemail2 = models.EmailField(max_length=254,null=True, blank=True, verbose_name="Email #2:")

    class Meta:
        unique_together = ["custfirstname", "custlastname", "custadd1", "custcity", "custst"]

    def get_absolute13_url(self):
        return f"/mhadatabase/{self.id}/customerpage/"

    def get_absolute12_url(self):
        return f"/mhadatabase/{self.custid}/customerpage/"

    def get_absolute4_url(self):
        return f"/mhadatabase/{self.custid}/newcust"

    def get_absolute_url6(self):
        return f"/mhadatabase/{self.conid}/dupconinfo"

    def get_absolute14_url(self):
        return f"/mhadatabase/{self.id}/jobselection"

    def get_absolute10_url(self):
        return f"/wscdatabase/{self.id}/addcust/"

    def get_absolute7_url(self):
        return f"/mhadatabase/{self.id}/newcust/"



class Addnew(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    addnews = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    def __str__(self):
        return self.addnews


class Man(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    manufacturer = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    def __str__(self):
        return self.manufacturer


class Type(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    types = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.types

class Config(models.Model):
    configs = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.configs



class Eff(models.Model):
    effs = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.effs


class Mfgmodeldescrip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    mfgmodeldescrips = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.mfgmodeldescrip


class Gasviv(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    gasvivs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.gasvivs


class Description(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    descriptions = models.TextField()

    def __str__(self):
        return self.descriptions


class Motortype(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    motortypes = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.motortypes


class Refrig(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    refrigs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.refrigs


class Btu(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    btus = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.btus


class Outputstg1(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    outputstg1s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.outputstg1s

class Outputstg2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    outputstg2s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.outputstg2s


class Outputstg3(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    outputstg3s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.outputstg3s


class Warr(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    warrs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.warrs


class Filtertype(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    typefilter = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.typefilter


class Filtermfg(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    mfgfilter = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.mfgfilter


class Filtereff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    efffilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.efffilter


class ConfigFurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    configs = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.configs


class ConfigCond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    configs = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.configs


class ConfigEvap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    configs = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.configs


class Furneff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    efffurn = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.efffurn


class Evapeff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    effevap = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.effevap


class Condeff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    effcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.effcond


class Mfgmodeldescripfurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnmfgmodeldescrip = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.furnmfgmodeldescrip


class Mfgmodeldescripcond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condmfgmodeldescrip = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.condmfgmodeldescrip


class Mfgmodeldescripevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapmfgmodeldescrip = models.CharField(max_length=45, verbose_name="")
    def __str__(self):
        return self.evapmfgmodeldescrip


class Gasvivfurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furngasvivs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furngasvivs


class Gasvivcond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condgasvivs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condgasvivs


class Gasvivevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapgasvivs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.evapgasvivs


class Motortypefurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnmotortypes = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnmotortypes


class Motortypecond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condmotortypes = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condmotortypes


class Motortypeevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapmotortypes = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.evapmotortypes


class Descriptionfurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furndescription = models.TextField()

    def __str__(self):
        return self.furndescription


class Descriptioncond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conddescriptions = models.TextField()

    def __str__(self):
        return self.conddescriptions


class Descriptionevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapdescriptions = models.TextField()

    def __str__(self):
        return self.evapdescriptions



class Refrigfurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnrefrigs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnrefrigs


class Refrigcond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condrefrigs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condrefrigs



class Refrigevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evaprefrigs = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.evaprefrigs


class BTUfurn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnbtus = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnbtus


class BTUcond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condbtus = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condbtus


class BTUevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapbtus = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.evapbtus


class Outputstg1furn(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnoutputstg1s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnoutputstg1s


class Outputstg1cond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condoutputstg1s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condoutputstg1s


class Outputstg1evap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    evapoutputstg1s = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.evapoutputstg1s

class Equipment(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(blank=True, null=True, default=None, verbose_name="bid ID.")
    addnew = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    type2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    config2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    configcond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    configevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    configfurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    configcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    configevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    efficiency2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    effcond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    effevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    effcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    efffurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    effevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescripcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescripfurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescripevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescrip2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescripcond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescripevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasvivcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasvivfurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasvivevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasviv2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasvivcond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    gasvivevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortypefurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortypecond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortypeevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortype2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortypecond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    motortypeevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    descriptionfurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    descriptioncond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    descriptionevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    description2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    descriptioncond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    descriptionevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrigfurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrigcond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrigevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrig2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrigcond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    refrigevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btufurn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btucond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btuevap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btu2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btucond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    btuevap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg1furn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg1cond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg1evap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg12 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg1cond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg1evap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg2furn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg2cond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg2evap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg22 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg2cond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg2evap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg3furn = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg3cond = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg3evap = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg32 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg3cond2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    outputstg3evap2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    warr = models.ForeignKey(Warr, to_field="id", blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="Part Warr:")
    warr2 = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    height = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="Height")
    width = models.DecimalField(decimal_places=2, max_digits=7, default=0.00,  verbose_name="Width")
    depth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00,  verbose_name="Depth")
    increasepercent = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    increasecost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    total_value = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")



    def total_cost(self):
        return self.cost * self.increasepercent

    def save(self, *args, **kwargs):
        # Ensure total_cost is calculated before saving, if needed
        self.total_cost_value = self.total_cost()
        super().save(*args, **kwargs)

    total_cost_value = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.cost} * {self.increasepercent} = {self.total_cost_value}"


    def get_absolute_url(self):
        return f"/mhadatabase/{self.modelnum}/modequip/"


    def get_absolute3_url(self):
        return f"/mhadatabase/{self.id}/addnewequip"



class Equipment2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(blank=True, null=True, default=None, verbose_name="bid ID.")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    mfg = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mfg:")
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type:")
    config = models.CharField(max_length=50, blank=True, null=True, verbose_name="Configuration")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    mfgmodeldescrip = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mfg Descrip.")
    gasviv = models.CharField(max_length=50, blank=True, null=True, verbose_name="Gas VIv")
    motortype = models.CharField(max_length=50, blank=True, null=True, verbose_name="Motor Type")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    refrig = models.CharField(max_length=50, blank=True, null=True, verbose_name="Refrig.")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    outputstg1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg1")
    outputstg2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg2")
    outputstg3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg3")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="Price")
    warr = models.CharField(max_length=225, blank=True, null=True, verbose_name="Part Warr:")
    height = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="Height")
    width = models.DecimalField(decimal_places=2, max_digits=7, default=0.00,  verbose_name="Width")
    depth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00,  verbose_name="Depth")
    increasepercent = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="increasepercent")
    increasecost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="increasecost")
    total_value = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="total_value")
    mfg2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mfg2:")
    type2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type2:")
    config2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="config2")
    eff2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="eff2")
    mfgmodeldescrip2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="mfgmodeldescrip2")
    gasviv2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="gasviv2")
    motortype2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="motortype2")
    description2 = models.CharField(max_length=225, blank=True, null=True, verbose_name="description2")
    refrig2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="refrig2")
    btu2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="btu2")
    outputstg12 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg1")
    outputstg22 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg2")
    outputstg32 = models.CharField(max_length=50, blank=True, null=True, verbose_name="outputstg3")
    warr2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Part Warr:")
    total_cost_value = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    smart = models.CharField(max_length=5, blank=True, null=True, verbose_name="")

    def __str__(self):
        return  str(self.modelnum)

    def get_absolute3_url(self):
        return f"/mhadatabase/{self.id}/addnewequip2"

    def get_absolute4_url(self):
        return f"/mhadatabase/{self.id}/editquip"

    def get_absolute5_url(self):
        return f"/mhadatabase/main"

    def get_absolute6_url(self):
        return f"/mhadatabase/updateequip"



class ManFilter(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    manufacturer = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.manufacturer


class EffFilter(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    eff = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.eff


class MfgmodeldescripFilter(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    mfgmodeldescrip = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.mfgmodeldescrip


class FilterMfgmodeldescrip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    Mfgmodeldescripfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.Mfgmodeldescripfilter


class FilterMfgmodeldescripcond(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    Mfgmodeldescripfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.Mfgmodeldescripfilter


class FilterMfgmodeldescripevap(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    Mfgmodeldescripfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.Mfgmodeldescripfilter


class EquipUpdate(models.Model):
    objects = None
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    type =  models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg =  models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    eff = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfgmodeldescrip = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    update = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def get_absolute_url(self):
        return f"/mha/updateequip"


class GlobalIncrease(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    increaseglobal = models.DecimalField(decimal_places=2, max_digits=3, default=0.00, unique=True, verbose_name="")


    def super__init__(self, increaseglobal):
        self.increaseglobal = Decimal(increaseglobal)

    def __str__(self):
        return str(self.increaseglobal)


class PercentMulti(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    increase =models.ForeignKey(GlobalIncrease, to_field="id", blank=True,  null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")


class PercentIncrease(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    percentage = models.DecimalField(decimal_places=2, max_digits=3, default=0.00, unique=True, verbose_name="")



class EquipUpdate1(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(null=True, blank=True, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    increasepercent = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    increasecost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    updatecost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")



class MaterialType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    type = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.type


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    mfg = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.mfg


class Vendor(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    vnr = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.vnr


class Material(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(null=True, default=None, verbose_name="")
    descrip = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, null=True, blank=True, default=0.00, verbose_name="")
    matmfg = models.ForeignKey(Manufacturer, to_field="id", blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    matmfg2= models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")
    vendor = models.ForeignKey(Vendor, to_field="id", blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    vendor2 = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")
    vendornum = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")
    materialtype = models.ForeignKey(MaterialType, to_field="id", blank=True, null=True, default=None,
                             on_delete=models.CASCADE, verbose_name="")
    materialtype2 = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.descrip

    def get_absolute10_url(self):
        return f"/mhadatabase/{self.id}/addnewmat"

    def get_absolute11_url(self):
        return f"/mhadatabase/{self.idA}/deletemat1"

    def get_absolute12_url(self):
        return f"/mhadatabase/{self.idA}/editmat"

    def get_absolute13_url(self):
        return f"/mhadatabase/{self.idA}/editmat"


class MatUpdate(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    descrip = models.IntegerField(null=True, blank=True, verbose_name="")
    mfg = models.IntegerField(null=True, blank=True, verbose_name="")
    vendor = models.IntegerField(null=True, blank=True, verbose_name="")
    materialtype = models.IntegerField(null=True, blank=True, verbose_name="")


class JobLocation(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    jobloc = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.jobloc


class FurnaceType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furntype = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.furntype


class OutsideUnitType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    outsidetype = models.CharField(max_length=75, null=True, blank=True, default=None, verbose_name="")

    def __str__(self):
        return self.outsidetype


class FilterCondEff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condefffilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condefffilter


class FilterCondbtu(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condbtufilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condbtufilter


class FilterCondDescrip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conddescripfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.conddescripfilter


class FilterCondModelnum(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    condmodelnumfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.condmodelnumfilter


class FilterFurnbtu(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnbtufilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnbtufilter


class FilterFurnConfig(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnconfigfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnconfigfilter


class FilterFurnEff(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnefffilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furnefffilter


class FilterFurnDescrip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furndescripfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.furndescripfilter


class FilterFurnModelnum(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furnmodelnumfilter = models.CharField(max_length=45, verbose_name="")
    furnwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    furnheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


    def __str__(self):
        return self.furnmodelnumfilter


class FilterCoilAll(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    coiltype = models.CharField(max_length=25, null=True, blank=True, default=None, verbose_name="")
    coilbtu = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    coilconfig = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    coilmodnum = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    coilheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    coilwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class FilterCoiltype(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    coiltypefilter = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.coiltypefilter


class FilterCoilbtu(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    coilbtufilter = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.coilbtufilter


class FilterCoilConfig(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    coilconfigfilter = models.CharField(max_length=45, verbose_name="")

    def __str__(self):
        return self.coilconfigfilter


class FilterCoilModelnum(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    coilmodelnumfilter = models.CharField(max_length=45, verbose_name="")
    coilwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    coilheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


    def __str__(self):
        return self.coilmodelnumfilter


class FilterThermostat(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    thermomfg = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.thermomfg


class FilterThermostatModnum(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    thermomodnum = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    smart = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.thermomodnum



class Efficiency2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    efficiencys = models.IntegerField(null=True, default=None, verbose_name="")
    def __str__(self):
        return self.efficiencys


class RebateInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    furn95 = models.IntegerField(null=True, default=None, verbose_name="")
    furn97 = models.IntegerField(null=True, default=None, verbose_name="")
    furntherm95 = models.IntegerField(null=True, default=None, verbose_name="")
    furntherm97 = models.IntegerField(null=True, default=None, verbose_name="")
    smartthermnicor = models.IntegerField(null=True, default=None, verbose_name="")
    smartthermcomed = models.IntegerField(null=True, default=None, verbose_name="")

class NicorRebate1(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rebate1eff = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

class NicorRebate2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rebate2eff = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

class NicorRebate3(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rebate3eff = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

class NicorRebate4(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rebate4eff = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

class NicorRebate5(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    rebate5eff = models.CharField(max_length=45, blank=True, null=True, verbose_name="")





class EquipSelection(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bidid = models.IntegerField(null=True, default=None, verbose_name="BidID.")
    conid =  models.IntegerField(null=True, default=None, verbose_name="ConID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="CustID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="JobID.")
    bididA = models.IntegerField(null=True, default=None, verbose_name="BidIDA.")
    joblocation = models.CharField(null=True, blank=True, max_length=45, verbose_name="Job Location:")
    furntype = models.CharField(null=True, blank=True, max_length=45, verbose_name="Furnace Type:")
    furnmodrebatenum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furnmodnum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furnconfig = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furndescript = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furneff = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furnbtub = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furnbtu = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    furnwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    furnheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    furndepth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    odmodrebatenum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    condmodnum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    conddescript = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    condeff = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    condbtu = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    condbtub = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilmfg = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilmodrebatenum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilmodnum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coiltype = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilconfig = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilbtu = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilbtub = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    coilwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    coilheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    coildepth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    furncoilheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    targetseerrating = models.IntegerField(null=True, default=None, verbose_name="")
    targetseerratingB = models.IntegerField(null=True, default=None, verbose_name="")
    equipcomboseerRate = models.IntegerField(null=True, default=None, verbose_name="")
    vendor1rebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    vendor2rebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    vendor3rebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    vendor4rebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    smart = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    ahriref = models.IntegerField(null=True, default=None, verbose_name="")
    lock = models.CharField(max_length=45, verbose_name="")
    thermostatgroup = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    airhandlertype = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    outsideunittype = models.CharField(null=True, blank=True, max_length=45, verbose_name="Outside Unit Type")
    thermostatb = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    thermostat = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    thermostatmodnum = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    vendor4rebate2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totalrebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    eqmtrtype = models.CharField(max_length=45, verbose_name="")
    plenumheight = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    plenumwidth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    plenumdepth = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    acunitrebateamount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    furnunitrebateamount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    commedfurnthermbonus = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    commedbonus = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def get_absolute11_url(self):
        return f"/mhadatabase/{self.custid}/jobselection"

    def get_absolute16_url(self):
        return f"/mhadatabase/{self.custid}/jobselection"

    def get_absolute17_url(self):
        return f"/mhadatabase/{self.jobid}/equipselection1"

    def get_absolute7_url(self):
        return f"/mhadatabase/{self.custid}/customerpage/"

    def get_absolute18_url(self):
        return f"/mhadatabase/{self.jobid}/customerinfo"

    def get_absolute19_url(self):
        return f"/mhadatabase/{self.bidid}/bidpage/"

    def get_absolute20_url(self):
        return f"/mhadatabase/{self.id}/equipselection2"





class FilterEquipType(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    typeequip = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return self.typeequip


class FilterTypeDescrip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    mfg = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    modnum = models.CharField(max_length=45, blank=True, null=True, verbose_name="")
    mfgdescrip = models.CharField(max_length=45, blank=True, null=True, verbose_name="")

    def __str__(self):
        return f"{self.modnum} - {self.mfgdescrip}"



class Bidding(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bidid = models.IntegerField(null=True,default=None, verbose_name="BidID.")
    conid =  models.IntegerField(null=True, default=None, verbose_name="ConID.")
    custid = models.IntegerField(null=True,default=None, verbose_name="CustID.")
    jobid = models.IntegerField(null=True,default=None, verbose_name="JobID.")
    bididA = models.IntegerField(null=True,default=None, verbose_name="BidIDA.")
    joblocation = models.CharField(max_length=45, verbose_name="Job Location:")
    optionsid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    options = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    jobtype1 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript1 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost1total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity1 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype2 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript2 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost2total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity2 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype3 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript3 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost3total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity3 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype4 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript4 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost4total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity4 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype5 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    jobtype5b = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript5 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript5b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost5total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity5 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype6 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    jobtype6b = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript6 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript6b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost6total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity6 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    jobtype7 = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    jobtype7b = models.CharField(max_length=45, null=True, blank=True, verbose_name="")
    descript7 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript7b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost7total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity7 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript8 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript8b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost8total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity8 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript9 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript9b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost9total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity9 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript10 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript10b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost10total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity10 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript11 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript11b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost11total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity11 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript12 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript12b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost12total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity12 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript13 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript13b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost13total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity13 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript14 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript14b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost14total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity14 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript15 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript15b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost15total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity15 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript16 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript16b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost16total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity16 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript17 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript17b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost17total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity17 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript18 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript18b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost18total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity18 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript19 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript19b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost19total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity19 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript20 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript20b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost20total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity20 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript21 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript21b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost21total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity21 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript22 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript22b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost22total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity22 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript23 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript23b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost23total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity23 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript24 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript24b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost24total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity24 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript25 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript25b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost25total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity25 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript26 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript26b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost26total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity26 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript27 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript27b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost27total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity27 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript28 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript28b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost28total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity28 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript29 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript29b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost29total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity29 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript30 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript30b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost30total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity30 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript31 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript31b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost31total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity31 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript32 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript32b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost32total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity32 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript33 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript33b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost33total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity33 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript34 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript34b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost34total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity34 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript35 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript35b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost35total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity35 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript36 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript36b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost36total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity36 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript37 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript37b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost37total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity37 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript38 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript38b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost38total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity38 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript39 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript39b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost39total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity39 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript40 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript40b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost40total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity40 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript41 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript41b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost41total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity41 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript42 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript42b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost42total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity42 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript43 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript43b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost43total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity43 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript44 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript44b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost44total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity44 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript45 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript45b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost45total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity45 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    descript46 = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    descript46b = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    cost46total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    quanity46 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    mattype = models.CharField(max_length=45, null=True, blank=True,verbose_name="")
    matwholeprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    equipwholeprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    subwholeprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    locationtotal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techlevel = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    techrate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techhrs = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techlevel2 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    techrate2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techhrs2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techlevel3 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    techrate3 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techhrs3 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techlevel4 = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    techrate4 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    techhrs4 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    directlaborcost1 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    directlaborcost2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    directlaborcost3 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    directlaborcost4 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    notes = models.CharField(max_length=255, verbose_name="")
    proposaldate = models.DateField(auto_now_add=False, auto_now=True, blank=True, verbose_name="")
    esaquanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    esaamount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    esacost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    warrdescript = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    warramount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    bidcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    thermoqualify = models.CharField(max_length=255, verbose_name="")
    datetime = models.DateField(auto_now_add=False, auto_now=True, blank=True, verbose_name="")
    equipcomboseerrate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    revisiondate  = models.DateField(auto_now_add=False, auto_now=True, blank=True, verbose_name="")
    lock = models.CharField(max_length=255, verbose_name="")
    thermostatgroup = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    osrdescrip = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    osrunitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    osrvendor = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    osrdescripb = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    osrunitpriceb = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    osrvendorb = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    count = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def get_absolute27_url(self):
        return f"/mhadatabase/{self.bidid}/bidpage"

    def get_absolute28_url(self):
        return f"/mhadatabase/main"


class Quanity(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quanitynum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.quanitynum)


class OutsideResource(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="JobID.")
    osrdescrip = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    osrunitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    osrvendor = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.osrdescrip)


class MatTypeBid(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    type = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def __str__(self):
        return str(self.type)


class Package(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    package = models.CharField(max_length=75, verbose_name="")
    packagecost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def __str__(self):
        return str(self.package)



class TechLevel(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    level = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    rate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def __str__(self):
        return str(self.level)


class TechHours(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    hrstech = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def __str__(self):
        return str(self.hrstech)


class InstallPackage1(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute_url(self):
        return f"/mhadatabase/updateequip"

    def get_absolute1a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage1"

    def get_absolute1b_url(self):
        return f"/mhadatabase/{self.id}/deletepackage1a"

    def get_absolute1c_url(self):
        return f"/mhadatabase/package1"



class InstallPackage1Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)



class InstallPackage2(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute2a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage2"


class InstallPackage2Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage3(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute3a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage3"


class InstallPackage3Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)



class InstallPackage4(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute4a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage4"


class InstallPackage4Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage5(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute5a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage5"


class InstallPackage5Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage6(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute6a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage6"


class InstallPackage6Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)

class InstallPackage7(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute7a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage7"


class InstallPackage7Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage8(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute8a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage8"


class InstallPackage8Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage9(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute9a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage9"


class InstallPackage9Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage10(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute10a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage10"


class InstallPackage10Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage11(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute11a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage11"


class InstallPackage11Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)



class InstallPackage12(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute12a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage12"


class InstallPackage12Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage13(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute13a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage13"


class InstallPackage13Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage14(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute14a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage14"


class InstallPackage14Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage15(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute15a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage15"


class InstallPackage15Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)


class InstallPackage16(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    quant = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    description = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    unitprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    matid = models.IntegerField(blank=True, null=True, default=None, verbose_name="")

    def __str__(self):
        return str(self.description)

    def get_absolute16a_url(self):
        return f"/mhadatabase/{self.id}/deletepackage16"


class InstallPackage16Name(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    packagenum = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    name = models.CharField(null=True, blank=True, max_length=45, verbose_name="")

    def __str__(self):
        return str(self.name)



class Contract(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bidid = models.IntegerField(null=True, default=None, verbose_name="BidID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="ConID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="CustID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="JobID.")
    contractdate = models.DateField(blank=True, null=True)
    downpaymentdate = models.DateField(blank=True, null=True)
    finalpaymentdate = models.DateField(blank=True, null=True)
    depositterms = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    finalterms = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    deposit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    finalpayment = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    costbeforrebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totaljobcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totalrebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    grandtotalcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    depositperc = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    memo1 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo2 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo3 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo4 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo5 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo6 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo7 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo8 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo9 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo10 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo11 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo12 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo13 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo14 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo15 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo16 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo17 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo18 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo19 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo20 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo21 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo22 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo23 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo24 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo25 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo26 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo27 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo28 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo29 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo30 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")
    memo31 = models.CharField(max_length=254, default=None, null=True, blank=True, verbose_name="")



class CurrentJobInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    bidid = models.IntegerField(null=True, default=None, verbose_name="BidID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="ConID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="CustID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="JobID.")
    currentlocrm = models.CharField(max_length=60, blank=True, verbose_name="")
    options = models.CharField(max_length=60, blank=True, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    locationcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    rebatetotal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    loccostafterrebate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    acceptcontract = models.BooleanField(verbose_name="Room Active", default=True)
    sd = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    sdtotal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    sdrate = models.IntegerField(null=True, default=None, verbose_name="")
    count = models.IntegerField(null=True, default=None, verbose_name="JobID.")


    def get_absolute18_url(self):
        return f"/mhadatabase/{self.jobid}/bidpage"


class PackageInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    id1 = models.IntegerField(null=True, default=None, verbose_name="")
    name1 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name1b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost1 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id2 = models.IntegerField(null=True, default=None, verbose_name="")
    name2 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name2b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id3 = models.IntegerField(null=True, default=None, verbose_name="")
    name3 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name3b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost3 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id4 = models.IntegerField(null=True, default=None, verbose_name="")
    name4 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name4b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost4 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id5 = models.IntegerField(null=True, default=None, verbose_name="")
    name5 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name5b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost5 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id6 = models.IntegerField(null=True, default=None, verbose_name="")
    name6 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name6b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost6 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id7 = models.IntegerField(null=True, default=None, verbose_name="")
    name7 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name7b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost7 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id8 = models.IntegerField(null=True, default=None, verbose_name="")
    name8 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name8b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost8 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id9 = models.IntegerField(null=True, default=None, verbose_name="")
    name9 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name9b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost9 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id10 = models.IntegerField(null=True, default=None, verbose_name="")
    name10 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name10b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost10 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id11 = models.IntegerField(null=True, default=None, verbose_name="")
    name11 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name11b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost11 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id12 = models.IntegerField(null=True, default=None, verbose_name="")
    name12 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name12b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost12 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id13 = models.IntegerField(null=True, default=None, verbose_name="")
    name13 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name13b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost13 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id14 = models.IntegerField(null=True, default=None, verbose_name="")
    name14 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name14b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost14 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id15 = models.IntegerField(null=True, default=None, verbose_name="")
    name15 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name15b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost15 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    id16 = models.IntegerField(null=True, default=None, verbose_name="")
    name16 = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    name16b = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    cost16 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def get_absolute1_url(self):
        return f"/mhadatabase/{self.id}/changename1"

    def get_absolute2_url(self):
        return f"/mhadatabase/{self.id}/changename2"

    def get_absolute3_url(self):
        return f"/mhadatabase/{self.id}/changename3"

    def get_absolute4_url(self):
        return f"/mhadatabase/{self.id}/changename4"

    def get_absolute5_url(self):
        return f"/mhadatabase/{self.id}/changename5"

    def get_absolute6_url(self):
        return f"/mhadatabase/{self.id}/changename6"

    def get_absolute7_url(self):
        return f"/mhadatabase/{self.id}/changename7"

    def get_absolute8_url(self):
        return f"/mhadatabase/{self.id}/changename8"

    def get_absolute9_url(self):
        return f"/mhadatabase/{self.id}/changename9"

    def get_absolute10_url(self):
        return f"/mhadatabase/{self.id}/changename10"

    def get_absolute11_url(self):
        return f"/mhadatabase/{self.id}/changename11"

    def get_absolute12_url(self):
        return f"/mhadatabase/{self.id}/changename12"

    def get_absolute13_url(self):
        return f"/mhadatabase/{self.id}/changename13"

    def get_absolute14_url(self):
        return f"/mhadatabase/{self.id}/changename14"

    def get_absolute15_url(self):
        return f"/mhadatabase/{self.id}/changename15"

    def get_absolute16_url(self):
        return f"/mhadatabase/{self.id}/changename16"


class TotalJobCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    descripid = models.CharField(max_length=60, blank=True, default=None, verbose_name="")
    jobcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class SelectedEquip(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    equipid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type:")
    mfg = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mfg:")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    mfgmodeldescrip = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mfg Descrip.")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    warr = models.CharField(max_length=70, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")



class DetailTable(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    details = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type:")

    def __str__(self):
        return str(self.details)


class Terms(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    term = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type:")

    def __str__(self):
        return str(self.term)


class Option(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="")
    option = models.CharField(max_length=50, blank=True, null=True, verbose_name="")


class Custpagelocation(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    joblocation = models.CharField(null=True, blank=True, max_length=45, verbose_name="Job Location:")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute21_url(self):
        return f"/mhadatabase/{self.custid}/customerinfo"


class multiformA(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class multiformB(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class multiformC(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class multiformD(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class multiformE(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    optionid = models.IntegerField(null=True, default=None, verbose_name="")
    options = models.CharField(null=True, blank=True, max_length=45, verbose_name="")
    quanity = models.IntegerField(blank=True, null=True, default=None, verbose_name="")
    type = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    mfg = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    modelnum = models.CharField(max_length=50, blank=True, null=True, verbose_name="Model #:")
    description = models.CharField(max_length=225, blank=True, null=True, verbose_name="Description")
    eff = models.CharField(max_length=50, blank=True, null=True, verbose_name="Efficiency")
    btu = models.CharField(max_length=50, blank=True, null=True, verbose_name="BTU's")
    cost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class Tax(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    taxrate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class JobCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    matcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    taxrate = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    salestax = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totalmatcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    directlaborcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    ohlabor = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    totallaborcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    netjobcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    netprofit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    netprofitcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    netjobcost2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    netjobcost3 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    subtotal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    percenatage = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    targetnetprofit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    Seasonaldiscount = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    costplusprofit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    subcontractors = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    instantrebate1 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    instantrebate2 = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    jobcostprice = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    rebateamouint = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    finaljobcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    OSRcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class MatCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    descript = models.IntegerField(null=True, default=None, verbose_name="")
    matcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class OSRCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    descript = models.IntegerField(null=True, default=None, verbose_name="")
    OSRcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class laborCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    descript = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="")
    laborcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class EquipmentCost(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    conid = models.IntegerField(null=True, default=None, verbose_name="")
    custid = models.IntegerField(null=True, default=None, verbose_name="")
    jobid = models.IntegerField(null=True, default=None, verbose_name="")
    bidid = models.IntegerField(null=True, default=None, verbose_name="")
    descript = models.IntegerField(null=True, default=None, verbose_name="")
    equipcost = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")


class Calculation(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    netprofit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    ohlabor = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")
    salestax = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

class Profit(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    netprofit = models.DecimalField(decimal_places=2, max_digits=7, default=0.00, verbose_name="")

    def __str__(self):
        return str(self.netprofit)