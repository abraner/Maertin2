from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import CustomerInfo, ContractorInfo, Equipment, Equipment2, Man, Type,  Gasvivfurn, \
Motortypefurn, Motortypecond, Motortypeevap, Descriptionfurn, Descriptioncond, Descriptionevap, Refrigfurn, \
Refrigcond, Refrigevap,  BTUfurn, BTUcond, BTUevap, Outputstg1furn, Outputstg1cond, Outputstg1evap, Warr, EquipUpdate, \
PercentMulti, Material, EquipSelection, Condeff, ConfigCond, ConfigEvap, ConfigFurn, Evapeff, Furneff, Mfgmodeldescripcond, \
Mfgmodeldescripevap, Mfgmodeldescripfurn, Gasvivcond, Gasvivevap, Gasvivfurn, EffFilter, FilterMfgmodeldescrip, ManFilter, \
FilterMfgmodeldescripcond, FilterMfgmodeldescripevap, Config, Eff, Mfgmodeldescrip, Description, Gasviv, Motortype, \
Refrig, Btu, Outputstg1, Outputstg2, Outputstg3, MfgmodeldescripFilter, JobLocation, FurnaceType, OutsideUnitType, \
Efficiency2, FilterCondEff, FilterCondbtu, FilterCondDescrip, FilterCondModelnum, FilterFurnbtu, FilterFurnConfig, \
FilterFurnEff, FilterFurnDescrip, FilterFurnModelnum, FilterCoilbtu, FilterCoilConfig, FilterCoilModelnum, \
    FilterThermostat, FilterThermostatModnum, FilterCoiltype, Bidding, FilterEquipType, Quanity, OutsideResource, \
MatTypeBid, FilterTypeDescrip, MaterialType, TechLevel, TechHours, InstallPackage1, InstallPackage2, InstallPackage3, \
InstallPackage4, InstallPackage5, InstallPackage6, InstallPackage7, InstallPackage8, InstallPackage9, InstallPackage10, \
InstallPackage11, InstallPackage12, InstallPackage13, InstallPackage14, InstallPackage15, InstallPackage16, PackageInfo, \
Contract, DetailTable, Terms, CurrentJobInfo, JobCost, Profit
from django.forms import modelformset_factory




FORMAT_CHOICES = (
    ('xls', 'xls'),
    ('csv', 'csv'),
)

class FormatForm(forms.Form):
    format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select(attrs={'class':'form-select'}))


class Coninfo(forms.ModelForm):
    class Meta:
        model = ContractorInfo
        fields = [
            'id',
            'conid',
            'concompanytname',
            'confirstname',
            'conlastname',
            'conadd1',
            'conadd2',
            'concity',
            'const',
            'conzipcode',
            'conwork1',
            'conwork2',
            'concell1',
            'concell2',
            'conhome',
            'conemail1',
            'conemail2',
        ]

        widgets = {'conwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class ConinfoB(forms.ModelForm):
    class Meta:
        model = ContractorInfo
        fields = [
            'concompanytname',
            'confirstname',
            'conlastname',
            'conadd1',
            'conadd2',
            'concity',
            'const',
            'conzipcode',
            'conwork1',
            'conwork2',
            'concell1',
            'concell2',
            'conhome',
            'conemail1',
            'conemail2',
        ]

        widgets = {'conwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'concell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'conhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }



class Custinfo(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'id',
            'custid',
            'conid',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }



class CustinfoB(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]

        widgets = {'custwork1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custwork2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell1': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custcell2': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   'custhome': forms.TextInput(attrs={'data-mask': "000-000-0000"}),
                   }


class DupConInfo(forms.ModelForm):

    class Meta:
        model = CustomerInfo
        fields = [
            'custid',
            'conid',
        ]



class EquipInfo(forms.ModelForm):

    effcond = forms.ModelChoiceField(queryset=Condeff.objects.all(), empty_label="Condenser Efficiency")
    effevap = forms.ModelChoiceField(queryset=Evapeff.objects.all(), empty_label="Evap. Efficiency")
    efffurn = forms.ModelChoiceField(queryset=Furneff.objects.all().order_by('-efffurn'), empty_label="Furnace Efficiency")
    configcond = forms.ModelChoiceField(queryset=ConfigCond.objects.all(), empty_label="Condenser Configuation")
    configevap = forms.ModelChoiceField(queryset=ConfigEvap.objects.all(), empty_label="Evaporation Coil Configuation")
    configfurn = forms.ModelChoiceField(queryset=ConfigFurn.objects.all().order_by('configs'), empty_label="Furnace Configuation")
    mfgmodeldescripcond = forms.ModelChoiceField(queryset=Mfgmodeldescripcond.objects.all(), empty_label="Condenser Description")
    mfgmodeldescripevap = forms.ModelChoiceField(queryset=Mfgmodeldescripevap.objects.all(), empty_label="Evaporation Coil Description")
    mfgmodeldescripfurn = forms.ModelChoiceField(queryset=Mfgmodeldescripfurn.objects.all().order_by('furnmfgmodeldescrip'), empty_label="Furnace Description")
    gasvivcond = forms.ModelChoiceField(queryset=Gasvivcond.objects.all(), empty_label="Condenser Gas Viv")
    gasvivevap = forms.ModelChoiceField(queryset=Gasvivevap.objects.all(), empty_label="Evaporation Gas Viv")
    gasvivfurn = forms.ModelChoiceField(queryset=Gasvivfurn.objects.all(), empty_label="Furnace Gas Viv")

    motortypecond = forms.ModelChoiceField(queryset=Motortypecond.objects.all(), empty_label="Condenser Motor Type")
    motortypeevap = forms.ModelChoiceField(queryset=Motortypeevap.objects.all(), empty_label="Evaporation Motor Type")
    motortypefurn = forms.ModelChoiceField(queryset=Motortypefurn.objects.all(), empty_label="Furnace Motor Type")

    descriptioncond = forms.ModelChoiceField(queryset=Descriptioncond.objects.all(), empty_label="Condenser Description")
    descriptionevap = forms.ModelChoiceField(queryset=Descriptionevap.objects.all(), empty_label="Evaporation Description")
    descriptionfurn = forms.ModelChoiceField(queryset=Descriptionfurn.objects.all(), empty_label="Furnace Description")

    refrigcond = forms.ModelChoiceField(queryset=Refrigcond.objects.all(), empty_label="Condenser Refrig.")
    refrigevap = forms.ModelChoiceField(queryset=Refrigevap.objects.all(), empty_label="Evaporation Refrig")
    refrigfurn = forms.ModelChoiceField(queryset=Refrigfurn.objects.all(), empty_label="Furnace Refrig")

    btucond = forms.ModelChoiceField(queryset=BTUcond.objects.all(), empty_label="Condenser BTU")
    btuevap = forms.ModelChoiceField(queryset=BTUevap.objects.all(), empty_label="Evaporation BTU")
    btufurn = forms.ModelChoiceField(queryset=BTUfurn.objects.all(), empty_label="Furnace BTU")

    outputstg1cond = forms.ModelChoiceField(queryset=Outputstg1cond.objects.all(), empty_label="Condenser Output Stage 1")
    outputstg1evap = forms.ModelChoiceField(queryset=Outputstg1evap.objects.all(), empty_label="Evaporation Output Stage 1")
    outputstg1furn = forms.ModelChoiceField(queryset=Outputstg1furn.objects.all(), empty_label="Furnace Output Stage 1")

    outputstg2cond = forms.ModelChoiceField(queryset=Outputstg1cond.objects.all(), empty_label="Condenser Output Stage 2")
    outputstg2evap = forms.ModelChoiceField(queryset=Outputstg1evap.objects.all(), empty_label="Evaporation Output Stage 2")
    outputstg2furn = forms.ModelChoiceField(queryset=Outputstg1furn.objects.all(), empty_label="Furnace Output Stage 2")

    outputstg3cond = forms.ModelChoiceField(queryset=Outputstg1cond.objects.all(), empty_label="Condenser Output Stage 3")
    outputstg3evap = forms.ModelChoiceField(queryset=Outputstg1evap.objects.all(), empty_label="Evaporation Output Stage 3")
    outputstg3furn = forms.ModelChoiceField(queryset=Outputstg1furn.objects.all(), empty_label="Furnace Output Stage 3")



    class Meta:
        model = Equipment
        fields = [
            'id',
            'idA',
            'modelnum',
            'mfg',
            'mfg2',
            'type',
            'type2',
            'config2',
            'configcond2',
            'configevap2',
            'configcond',
            'configevap',
            'configfurn',
            'efficiency2',
            'effcond2',
            'effevap2',
            'effcond',
            'efffurn',
            'effevap',
            'mfgmodeldescripcond',
            'mfgmodeldescripfurn',
            'mfgmodeldescripevap',
            'mfgmodeldescrip2',
            'mfgmodeldescripcond2',
            'mfgmodeldescripevap2',
            'gasvivfurn',
            'gasvivcond',
            'gasvivevap',
            'gasviv2',
            'gasvivcond2',
            'gasvivevap2',
            'motortypefurn',
            'motortypecond',
            'motortypeevap',
            'motortype2',
            'motortypecond2',
            'motortypeevap2',
            'descriptionfurn',
            'descriptioncond',
            'descriptionevap',
            'description2',
            'descriptioncond2',
            'descriptionevap2',
            'refrigfurn',
            'refrigcond',
            'refrigevap',
            'refrig2',
            'refrigcond2',
            'refrigevap2',
            'btufurn',
            'btucond',
            'btuevap',
            'btu2',
            'btucond2',
            'btuevap2',
            'outputstg1furn',
            'outputstg1cond',
            'outputstg1evap',
            'outputstg12',
            'outputstg1cond2',
            'outputstg1evap2',
            'outputstg2furn',
            'outputstg2cond',
            'outputstg2evap',
            'outputstg22',
            'outputstg2cond2',
            'outputstg2evap2',
            'outputstg3furn',
            'outputstg3cond',
            'outputstg3evap',
            'outputstg32',
            'outputstg3cond2',
            'outputstg3evap2',
            'cost',
            'warr',
            'warr2',
            'height',
            'width',
            'depth',
            'increasepercent',
        ]
        widgets = {
            'description2': forms.Textarea(attrs={'cols': 48, 'rows': 3}),
            'height': forms.NumberInput(attrs={'required': False, 'value': ''}),
            'efficiency': forms.NumberInput(attrs={'required': False}),

        }



class EquipInfoEdit(forms.ModelForm):

    class Meta:
        model = Equipment2
        fields = [
            'id',
            'idA',
            'modelnum',
            'mfg',
            'type',
            'config',
            'eff',
            'mfgmodeldescrip',
            'gasviv',
            'motortype',
            'description',
            'refrig',
            'btu',
            'outputstg1',
            'outputstg2',
            'outputstg3',
            'cost',
            'warr',
            'height',
            'width',
            'depth',
        ]

    description = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: none;'}))
    warr = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: none;'}))



class EquipInfo2(forms.ModelForm):
    mfg = forms.ModelChoiceField(queryset=Man.objects.values_list('manufacturer', flat=True).distinct())
    type = forms.ModelChoiceField(queryset=Type.objects.values_list('types', flat=True).distinct())
    config = forms.ModelChoiceField(queryset=Config.objects.values_list('configs', flat=True).distinct())
    eff = forms.ModelChoiceField(queryset=Eff.objects.values_list('effs', flat=True).distinct())
    description = forms.ModelChoiceField(queryset=Description.objects.values_list('descriptions', flat=True).distinct())
    gasviv = forms.ModelChoiceField(queryset=Gasviv.objects.values_list('gasvivs', flat=True).distinct())
    mfgmodeldescrip = forms.ModelChoiceField(queryset=Mfgmodeldescrip.objects.values_list('mfgmodeldescrips', flat=True).distinct())
    motortype = forms.ModelChoiceField(queryset=Motortype.objects.values_list('motortypes', flat=True).distinct())
    refrig = forms.ModelChoiceField(queryset=Refrig.objects.values_list('refrigs', flat=True).distinct())
    btu = forms.ModelChoiceField(queryset=Btu.objects.values_list('btus', flat=True).distinct())
    outputstg1 = forms.ModelChoiceField(queryset=Outputstg1.objects.values_list('outputstg1s', flat=True).distinct())
    outputstg2 = forms.ModelChoiceField(queryset=Outputstg2.objects.values_list('outputstg2s', flat=True).distinct())
    outputstg3 = forms.ModelChoiceField(queryset=Outputstg3.objects.values_list('outputstg3s', flat=True).distinct())
    warr = forms.ModelChoiceField(queryset=Warr.objects.values_list('warrs', flat=True).distinct())

    class Meta:
        model = Equipment2
        fields = [
            'id',
            'idA',
            'modelnum',
            'mfg',
            'type',
            'config',
            'eff',
            'mfgmodeldescrip',
            'gasviv',
            'motortype',
            'description',
            'refrig',
            'btu',
            'outputstg1',
            'outputstg2',
            'outputstg3',
            'cost',
            'warr',
            'height',
            'width',
            'depth',
            'mfg2',
            'type2',
            'config2',
            'eff2',
            'mfgmodeldescrip2',
            'gasviv2',
            'motortype2',
            'description2',
            'refrig2',
            'btu2',
            'outputstg12',
            'outputstg22',
            'outputstg32',
            'warr2',
            'smart',

        ]



 #   def __init__(self, *args, **kwargs):
 #       super().__init__(*args, **kwargs)
#        self.fields['warr'].queryset = Warr.objects.exclude(warrs="Add New Warranty")



class MfgInfo(forms.ModelForm):

    class Meta:
        model = Man
        fields = [
            'id',
            'manufacturer',
        ]


class TypeInfo(forms.ModelForm):

    class Meta:
        model = Type
        fields = [
            'id',
            'types',
        ]



class UpdateEquipInfo(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.values_list('types', flat=True).distinct().exclude(id='1'))
    mfg = forms.ModelChoiceField(queryset=ManFilter.objects.values_list('manufacturer', flat=True).distinct().exclude(id='1'))
    eff = forms.ModelChoiceField(queryset=EffFilter.objects.values_list('eff', flat=True).distinct().exclude(id='1'))
    mfgmodeldescrip = forms.ModelChoiceField(queryset=MfgmodeldescripFilter.objects.values_list('mfgmodeldescrip', flat=True).distinct().exclude(id='1'))
    class Meta:
        model = EquipUpdate
        fields = [
            'id',
            'type',
            'mfg',
            'eff',
            'mfgmodeldescrip',
            'modelnum',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class JobInfoCurrent(forms.ModelForm):

    class Meta:
        model = CurrentJobInfo
        fields = '__all__'






class PercentageChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.increase * 100:.0f}%"


class IncreaseGlobal(forms.ModelForm):

    class Meta:
        model = PercentMulti
        fields = ['increase']


class InstallMaterial(forms.ModelForm):

    class Meta:
        model = Material
        fields = ['id',
                  'idA',
                  'descrip',
                  'cost',
                  'matmfg',
                  'vendor',
                  'vendornum',
                  'materialtype',
                  'matmfg2',
                  'vendor2',
                  'materialtype2'

                  ]

        widgets = {
            'form.cost': forms.NumberInput(attrs={'step': None}),
        }


class MaterialSearch(forms.ModelForm):

    class Meta:
        model = Material
        fields = [
                  'descrip',
                  'matmfg',
                  'vendor',
                  'materialtype',

                  ]


class EquipmentSelect(forms.ModelForm):

    class Meta:
        model = EquipSelection
        fields = [
                  'jobid',
                  'bidid',
                  'conid',
                  'custid',
                  'bididA',

                  ]


class EquipmentSelect1(forms.ModelForm):
    joblocation = forms.ModelChoiceField(queryset=JobLocation.objects.all(), empty_label="Select an option")
    furntype = forms.ModelChoiceField(queryset=FurnaceType.objects.all(), empty_label="Select an option")
    outsideunittype = forms.ModelChoiceField(queryset=OutsideUnitType.objects.all(), empty_label="Select an option")
    condeff = forms.ModelChoiceField(queryset=FilterCondEff.objects.all(), empty_label="Select an option")
    condbtu = forms.ModelChoiceField(queryset=FilterCondbtu.objects.all(), empty_label="Select an option")
    conddescript = forms.ModelChoiceField(queryset=FilterCondDescrip.objects.all(), empty_label="Select an option")
    condmodnum = forms.ModelChoiceField(queryset=FilterCondModelnum.objects.all(), empty_label="Select an option")
    furnbtu = forms.ModelChoiceField(queryset=FilterFurnbtu.objects.all(), empty_label="Select an option")
    furnconfig = forms.ModelChoiceField(queryset=FilterFurnConfig.objects.all(), empty_label="Select an option")
    furneff = forms.ModelChoiceField(queryset=FilterFurnEff.objects.all(), empty_label="Select an option")
    furndescript = forms.ModelChoiceField(queryset=FilterFurnDescrip.objects.all(), empty_label="Select an option")
    furnmodnum = forms.ModelChoiceField(queryset=FilterFurnModelnum.objects.all(), empty_label="Select an option")
    coilbtu = forms.ModelChoiceField(queryset=FilterCoilbtu.objects.all(), empty_label="Select an option")
    coilconfig = forms.ModelChoiceField(queryset=FilterCoilConfig.objects.all(), empty_label="Select an option")
    coilmodnum = forms.ModelChoiceField(queryset=FilterCoilModelnum.objects.all(), empty_label="Select an option")
    thermostat = forms.ModelChoiceField(queryset=FilterThermostat.objects.all(), empty_label="Select an option")
    thermostatmodnum = forms.ModelChoiceField(queryset=FilterThermostatModnum.objects.all(), empty_label="Select an option")
    coiltype = forms.ModelChoiceField(queryset=FilterCoiltype.objects.all(), empty_label="Select an option")


    class Meta:
        model = EquipSelection
        fields = [
                  'jobid',
                  'bidid',
                  'conid',
                  'custid',
                  'bididA',
                  'joblocation',
                  'furntype',
                  'furnmodrebatenum',
                  'furnmodnum',
                  'furnconfig',
                  'furndescript',
                  'furneff',
                  'furnbtub',
                  'furnbtu',
                  'furnwidth',
                  'furnheight',
                  'furndepth',
                  'odmodrebatenum',
                  'condmodnum',
                  'conddescript',
                  'condeff',
                  'condbtu',
                  'condbtub',
                  'coilmfg',
                  'coilmodrebatenum',
                  'coilmodnum',
                  'coiltype',
                  'coilconfig',
                  'coilbtu',
                  'coilbtub',
                  'coilwidth',
                  'coilheight',
                  'coildepth',
                  'furncoilheight',
                  'targetseerrating',
                  'targetseerratingB',
                  'equipcomboseerRate',
                  'vendor1rebate',
                  'vendor2rebate',
                  'vendor3rebate',
                  'vendor4rebate',
                  'ahriref',
                  'lock',
                  'thermostatgroup',
                  'airhandlertype',
                  'outsideunittype',
                  'thermostatb',
                  'thermostat',
                  'thermostatmodnum',
                  'vendor4rebate2',
                  'totalrebate',
                  'eqmtrtype',
                  'plenumheight',
                  'plenumwidth',
                  'plenumdepth',
                  'acunitrebateamount',
                  'furnunitrebateamount',
                  'commedfurnthermbonus',
                  'commedbonus',
                  'optionid',
                  'options',

        ]



class BidSelect(forms.ModelForm):

    jobtype5 = forms.ModelChoiceField(queryset=FilterEquipType.objects.all().order_by('typeequip'), empty_label="")
    jobtype6 = forms.ModelChoiceField(queryset=FilterEquipType.objects.all().order_by('typeequip'), empty_label="")
    jobtype7 = forms.ModelChoiceField(queryset=FilterEquipType.objects.all().order_by('typeequip'), empty_label="")

    descript5 = forms.ModelChoiceField(queryset=FilterTypeDescrip.objects.all().order_by('mfgdescrip'), empty_label="")
    descript6 = forms.ModelChoiceField(queryset=FilterTypeDescrip.objects.all().order_by('mfgdescrip'), empty_label="")
    descript7 = forms.ModelChoiceField(queryset=FilterTypeDescrip.objects.all().order_by('mfgdescrip'), empty_label="")

    #descript5 =  forms.ModelChoiceField(queryset=FilterTypeDescrip.objects.all(),
    #                                    to_field_name='modnum')


    quanity1 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity2 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity3 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity4 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity5 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity6 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity7 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")

    descript40 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")
    descript41 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")
    descript42 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")
    descript43 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")
    descript44 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")
    descript45 = forms.ModelChoiceField(queryset=OutsideResource.objects.all().order_by('osrdescrip'), empty_label="")

    quanity40 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity41 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity42 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity43 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity44 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity45 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")

    descript8 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript9 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript10 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript11 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript12 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript13 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript14 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript15 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript16 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript17 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript18 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")

    quanity8 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity9 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity10 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity11 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity12 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity13 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity14 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity15 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity16 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity17 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity18 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")

    descript19 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript20 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript21 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript22 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript23 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript24 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript25 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript26 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript27 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript28 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript29 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    
    quanity19 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity20 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity21 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity22 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity23 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity24 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity25 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity26 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity27 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity28 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity29 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")

    descript30 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript31 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript32 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript33 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript34 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript35 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript36 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript37 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript38 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript39 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")
    descript46 = forms.ModelChoiceField(queryset=MatTypeBid.objects.all().order_by('type'), empty_label="")

    quanity30 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity31 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity32 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity33 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity34 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity35 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity36 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity37 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity38 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity39 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")
    quanity46 = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="0")

    mattype = forms.ModelChoiceField(queryset=MaterialType.objects.all().order_by('id'), empty_label="")

    techlevel = forms.ModelChoiceField(queryset=TechLevel.objects.all().order_by('level'), empty_label="")
    techlevel2 = forms.ModelChoiceField(queryset=TechLevel.objects.all().order_by('level'), empty_label="")
    techlevel3 = forms.ModelChoiceField(queryset=TechLevel.objects.all().order_by('level'), empty_label="")
    techlevel4 = forms.ModelChoiceField(queryset=TechLevel.objects.all().order_by('level'), empty_label="")

    techhrs = forms.ModelChoiceField(queryset=TechHours.objects.all().order_by('hrstech'), empty_label="")
    techhrs2 = forms.ModelChoiceField(queryset=TechHours.objects.all().order_by('hrstech'), empty_label="")
    techhrs3 = forms.ModelChoiceField(queryset=TechHours.objects.all().order_by('hrstech'), empty_label="")
    techhrs4 = forms.ModelChoiceField(queryset=TechHours.objects.all().order_by('hrstech'), empty_label="")




    class Meta:
        model = Bidding
        fields = [
            'id',
            'bidid',
            'conid',
            'custid',
            'jobid',
            'bididA',
            'joblocation',
            'options',
            'quanity1',
            'quanity2',
            'quanity3',
            'quanity4',
            'quanity5',
            'quanity6',
            'quanity7',
            'quanity8',
            'quanity9',
            'quanity10',
            'quanity11',
            'quanity12',
            'quanity13',
            'quanity14',
            'quanity15',
            'quanity16',
            'quanity17',
            'quanity18',
            'quanity19',
            'quanity20',
            'quanity21',
            'quanity22',
            'quanity23',
            'quanity24',
            'quanity25',
            'quanity26',
            'quanity27',
            'quanity28',
            'quanity29',
            'quanity30',
            'quanity31',
            'quanity32',
            'quanity33',
            'quanity34',
            'quanity35',
            'quanity36',
            'quanity37',
            'quanity38',
            'quanity39',
            'quanity40',
            'quanity41',
            'quanity42',
            'quanity43',
            'quanity44',
            'quanity45',
            'quanity46',
            'descript1',
            'descript2',
            'descript3',
            'descript4',
            'descript5',
            'descript6',
            'descript7',
            'descript8',
            'descript8b',
            'descript9',
            'descript9b',
            'descript10',
            'descript10b',
            'descript11',
            'descript11b',
            'descript12',
            'descript13',
            'descript14',
            'descript15',
            'descript16',
            'descript17',
            'descript18',
            'descript19',
            'descript20',
            'descript21',
            'descript22',
            'descript23',
            'descript24',
            'descript25',
            'descript26',
            'descript27',
            'descript28',
            'descript29',
            'descript30',
            'descript31',
            'descript32',
            'descript33',
            'descript34',
            'descript35',
            'descript36',
            'descript37',
            'descript38',
            'descript39',
            'descript40',
            'descript40b',
            'descript41',
            'descript42',
            'descript43',
            'descript44',
            'descript45',
            'descript46',
            'descript46b',
            'descript12b',
            'descript13b',
            'descript14b',
            'descript15b',
            'descript16b',
            'descript17b',
            'descript18b',
            'descript19b',
            'descript20b',
            'descript21b',
            'descript22b',
            'descript23b',
            'descript24b',
            'descript25b',
            'descript26b',
            'descript27b',
            'descript28b',
            'descript29b',
            'descript30b',
            'descript31b',
            'descript32b',
            'descript33b',
            'descript34b',
            'descript35b',
            'descript36b',
            'descript37b',
            'descript38b',
            'descript39b',
            'jobtype1',
            'jobtype2',
            'jobtype3',
            'jobtype4',
            'jobtype5',
            'jobtype5b',
            'jobtype6',
            'jobtype7',
            'techlevel',
            'techrate',
            'techhrs',
            'techlevel2',
            'techrate2',
            'techhrs2',
            'techlevel3',
            'techrate3',
            'techhrs3',
            'techlevel4',
            'techrate4',
            'techhrs4',
            'directlaborcost1',
            'directlaborcost2',
            'directlaborcost3',
            'directlaborcost4',
            'notes',
            'esaquanity',
            'esaamount',
            'esacost',
            'warrdescript',
            'warramount',
            'bidcost',
            'thermoqualify',
            'equipcomboseerrate',
            'lock',
            'thermostatgroup',
            'mattype',
            'osrdescrip',
            'osrunitprice',
            'osrvendor',
            'osrdescripb',
            'osrunitpriceb',
            'osrvendorb',
            'count',

        ]


class OSR(forms.ModelForm):

    class Meta:
        model = OutsideResource
        fields = [
                  'id',
                  'osrdescrip',
                  'osrunitprice',
                  'osrvendor',

                  ]





class Package1(forms.ModelForm):
    class Meta:
        model = InstallPackage1
        fields = '__all__'


Package1a = modelformset_factory(InstallPackage1, form=Package1, extra=0)


class Package1b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage1
        fields = '__all__'




class Package2(forms.ModelForm):

    class Meta:
        model = InstallPackage2
        fields = '__all__'


Package2a = modelformset_factory(InstallPackage2, form=Package2, extra=0)


class Package2b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage2
        fields = '__all__'




class Package3(forms.ModelForm):

    class Meta:
        model = InstallPackage3
        fields = '__all__'


Package3a = modelformset_factory(InstallPackage3, form=Package3, extra=0)


class Package3b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage3
        fields = '__all__'



class Package4(forms.ModelForm):

    class Meta:
        model = InstallPackage4
        fields = '__all__'


Package4a = modelformset_factory(InstallPackage4, form=Package4, extra=0)


class Package4b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage4
        fields = '__all__'




class Package5(forms.ModelForm):
    class Meta:
        model = InstallPackage5
        fields = '__all__'


Package5a = modelformset_factory(InstallPackage5, form=Package5, extra=0)


class Package5b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage5
        fields = '__all__'


class Package6(forms.ModelForm):
    class Meta:
        model = InstallPackage6
        fields = '__all__'


Package6a = modelformset_factory(InstallPackage6, form=Package6, extra=0)


class Package6b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage6
        fields = '__all__'


class Package7(forms.ModelForm):
    class Meta:
        model = InstallPackage7
        fields = '__all__'


Package7a = modelformset_factory(InstallPackage7, form=Package7, extra=0)


class Package7b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage7
        fields = '__all__'


class Package8(forms.ModelForm):
    class Meta:
        model = InstallPackage8
        fields = '__all__'


Package8a = modelformset_factory(InstallPackage8, form=Package8, extra=0)


class Package8b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage8
        fields = '__all__'


class Package9(forms.ModelForm):
    class Meta:
        model = InstallPackage9
        fields = '__all__'


Package9a = modelformset_factory(InstallPackage9, form=Package9, extra=0)


class Package9b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage9
        fields = '__all__'


class Package10(forms.ModelForm):
    class Meta:
        model = InstallPackage10
        fields = '__all__'


Package10a = modelformset_factory(InstallPackage10, form=Package10, extra=0)


class Package10b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage10
        fields = '__all__'


class Package11(forms.ModelForm):
    class Meta:
        model = InstallPackage11
        fields = '__all__'


Package11a = modelformset_factory(InstallPackage11, form=Package11, extra=0)


class Package11b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage11
        fields = '__all__'


class Package12(forms.ModelForm):
    class Meta:
        model = InstallPackage12
        fields = '__all__'


Package12a = modelformset_factory(InstallPackage12, form=Package12, extra=0)


class Package12b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage12
        fields = '__all__'


class Package13(forms.ModelForm):
    class Meta:
        model = InstallPackage13
        fields = '__all__'


Package13a = modelformset_factory(InstallPackage13, form=Package13, extra=0)


class Package13b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage13
        fields = '__all__'


class Package14(forms.ModelForm):
    class Meta:
        model = InstallPackage14
        fields = '__all__'


Package14a = modelformset_factory(InstallPackage14, form=Package14, extra=0)


class Package14b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage14
        fields = '__all__'


class Package15(forms.ModelForm):
    class Meta:
        model = InstallPackage15
        fields = '__all__'


Package15a = modelformset_factory(InstallPackage15, form=Package15, extra=0)


class Package15b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage15
        fields = '__all__'


class Package16(forms.ModelForm):
    class Meta:
        model = InstallPackage16
        fields = '__all__'


Package16a = modelformset_factory(InstallPackage16, form=Package16, extra=0)


class Package16b(forms.ModelForm):
    description = forms.ModelChoiceField(queryset=Material.objects.all().order_by('descrip'), empty_label="")
    quant = forms.ModelChoiceField(queryset=Quanity.objects.all().order_by('quanitynum'), empty_label="")
    class Meta:
        model = InstallPackage16
        fields = '__all__'


class InfoPackage(forms.ModelForm):
    class Meta:
        model = PackageInfo
        fields = [
            'id1',
            'name1',
            'name1b',
            'cost1',
            'id2',
            'name2',
            'name2b',
            'cost2',
            'id3',
            'name3',
            'name3b',
            'cost3',
            'id4',
            'name4',
            'name4b',
            'cost4',
            'id5',
            'name5',
            'name5b',
            'cost5',
            'id6',
            'name6',
            'name6b',
            'cost6',
            'id7',
            'name7',
            'name7b',
            'cost7',
            'id8',
            'name8',
            'name8b',
            'cost8',
            'id9',
            'name9',
            'name9b',
            'cost9',
            'id10',
            'name10',
            'name10b',
            'cost10',
            'id11',
            'name11',
            'name11b',
            'cost11',
            'id12',
            'name12',
            'name12b',
            'cost12',
            'id13',
            'name13',
            'name13b',
            'cost13',
            'id14',
            'name14',
            'name14b',
            'cost14',
            'id15',
            'name15',
            'name15b',
            'cost15',
            'id16',
            'name16',
            'name16b',
            'cost16',

        ]


class ContractForm(forms.ModelForm):
    memo1 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo2 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo3 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo4 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo5 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo6 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo7 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo8 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo9 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo10 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo11 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo12 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo13 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo14 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo15 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo16 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo17 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    memo18 = forms.ModelChoiceField(queryset=DetailTable.objects.all().order_by('details'), empty_label="")
    depositterms = forms.ModelChoiceField(queryset=Terms.objects.all().order_by('term'), empty_label="")
    finalterms = forms.ModelChoiceField(queryset=Terms.objects.all().order_by('term'), empty_label="")



    class Meta:
        model = Contract
        fields = '__all__'



        contractdate = forms.DateField(
            widget=DatePickerInput(options={"format": "mm/dd/yyyy", "autoclose": True})
        )

        widgets = {
            'memo31': forms.Textarea(attrs={'cols': 80, 'rows': 5}),

        }









class Costjob(forms.ModelForm):
    netprofit = forms.ModelChoiceField(queryset=Profit.objects.all().order_by('netprofit'), empty_label="0")

    class Meta:
        model = JobCost
        fields = [
            'conid',
            'custid',
            'jobid',
            'bidid',
            'matcost',
            'taxrate',
            'salestax',
            'totalmatcost',
            'directlaborcost',
            'ohlabor',
            'totallaborcost',
            'netjobcost',
            'netprofit',
            'subtotal',
            'percenatage',
            'costplusprofit',
            'subcontractors',
            'instantrebate1',
            'instantrebate2',
            'jobcostprice',
            'rebateamouint',
            'finaljobcost',
            ]