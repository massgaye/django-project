from django.db import models

# Create your models here.

class Personne(models.Model):
	NumeroPersonne = models.AutoField(primary_key=True)
	Prenom = models.CharField(max_length=50,  verbose_name="Prénom de la personne")
	Nom = models.CharField(max_length=50, verbose_name="Nom de la personne")
	TYPE_SEXE = (
		('Garçon', 'Garçon'),
		('Fille', 'Fille'),
	)
	Sexe = models.CharField(max_length=10, choices=TYPE_SEXE, default='Garçon')
	Age = models.IntegerField()
	Nationalite = models.CharField(max_length=30)
	STRUCTURE_ACCEUIL = (
		('venu avec sa mère', 'venu avec sa mère'),
		('SAO', 'SAO'),
		('AEMO', 'AEMO'),
		('Famille', 'Famille'),
		('communauté', 'communauté'),
		('né à la Maison rose', 'né à la Maison rose'),
		('forces de l\' ordre','forces de l\'ordre'),
		('structures sanitaires', 'structures sanitaires'),
		('partenaires sociaux', 'partenaires sociaux'),
		('pouponnière', 'pouponnière'),
		('médias', 'médias'),
		('venu d\'elle/de lui-même', 'venu d\'elle/de lui-même'),
		('autres', 'autres'), 
	)
	StructureAcceuil = models.CharField(max_length=50, choices=STRUCTURE_ACCEUIL, default='SAO', verbose_name="Structure d'acceuil") 
	
	SuiviInfo = models.CharField(max_length=100, verbose_name="Informations de suivi")
	ETHNIE = (
		('wolof','wolof'),
		('sérére','sérére'),
		('diola','diola'),
		('lébou','lébou'),
		('toucouleur','toucouleur'),
		('peul','peul'),
		('bambara/manding','bambara/manding'),
		('manjack','manjack'),
		('soninké','soninké'),
		('autres','autres'),
		('NSP','NSP'),
		('sous-régions','sous-régions'),
		('afrique','afrique'),
	)
	
	Ethnie = models.CharField(max_length=50, choices=ETHNIE, default='wolof')
	TYPE_SIGNALEMENT = (
		('Direct','Direct'),
		('Téléphone','Téléphone'),
		('déclaration de recherche','déclaration de recherche'),
	)
	TypeSignalement = models.CharField(max_length=50, choices=TYPE_SIGNALEMENT, default='Direct', verbose_name="Type de signalement")
	DateSignalement = models.DateTimeField(verbose_name="Date et heure du signalement")
	IdAppelant = models.ForeignKey('Appelant')
	#IdSituation = models.ManyToManyField('Situation')
	
	

	def __unicode__(self):
		return "{0} {{1}} {{2}} {{3}} {{4}} {{5}} {{6}} {{7}} {{8}} {{9}} {{10}} [{11}]".format(self.Personne.NumeroPersonne, self.Personne.Prenom, self.Personne.Nom, self.Personne.Sexe, self.Personne.Age, sel.Personne.Nationalite, self.Personne.StructureAcceuil, self.Personne.SuiviInfo, self.Personne.Ethnie, self.Personne.TypeSignalement, self.Personne.DateSignalement, self.Personne.IdAppelant)


class Situation(models.Model):
	IdSituation = models.AutoField(primary_key=True)
	LibelleSituation = models.CharField(max_length=50)
	IdTypeSituation = models.ForeignKey('TypeSituation')
	
	def __unicode__(self):
		return "{0} {{1}} [{2}]".format(self.Situation.IdSituation, self.Situation.LibelleSituation, self.Situation.IdTypeSituation)

class Centre(models.Model):
	IdCentre = models.AutoField(primary_key=True)
	NomCentre = models.CharField(max_length=50)
	AdresseCentre = models.CharField(max_length=50)
	Capacite = models.IntegerField()
	
	def __unicode__(self):
		return "{0} {{1}} {{2}} [{3}]".format(self.Centre.IdCentre, self.Centre.NomCentre, self.Centre.AdresseCentre, self.Centre.Capacite)

class TypeSituation(models.Model):
	IdTypeSituation = models.AutoField(primary_key=True)
	LibelleTypeSituation = models.CharField(max_length=50, verbose_name="Type de situation")
	
	def __unicode__(self):
		return "{0} [{1}]".format(self.TypeSituation.IdTypeSituation,  self.TypeSituation.LibelleTypeSituation)

class Service(models.Model):
	IdService = models.AutoField(primary_key=True)
	NatureService = models.CharField(max_length=50, verbose_name="Nature du service")
	LibelleService = models.CharField(max_length=50, verbose_name="Libellé du service reçu")

	def __unicode__(self):
		return "{0} {{1}} [{2}]".format(self.Service.IdService, self.Service.NatureService, self.Service.LibelleService)

class Appelant(models.Model):
	IdAppelant = models.AutoField(primary_key=True)
	PrenomAppelant = models.CharField(max_length=50, verbose_name="Prénom de la personne appelant")
	NomAppelant = models.CharField(max_length=50, verbose_name="Nom de la personne appelant")
	TelephoneAppelant = models.CharField(max_length=9, verbose_name="Téléphone de la personne appelant")
	VilleAppelant = models.CharField(max_length=30, verbose_name="Ville de la personne appelant")

	def __unicode__(self):
		return "{0} {{1}} {{2}} {{3}} [{4}]".format(self.Appelant.IdAppelant, self.Appelant.PrenomAppelant, self.Appelant.NomAppelant , self.Appelant.TelephoneAppelant, self.Appelant.VilleAppelant)

class Appel(models.Model):
	IdAppel = models.AutoField(primary_key=True)
	DateAppel = models.DateTimeField(verbose_name="Date et heure de l'appel")
	IdAppelant = models.ForeignKey('Appelant')

	def __unicode__(self):
		return "{0} {{1}} [{2}]".format(self.Appel.IdAppel, self.Appel.DateAppel, self.Appel.IdAppelant)

class Hebergement(models.Model):
	NumeroPersonne = models.ForeignKey('Personne')
	IdCentre = models.ForeignKey('Centre')
	DateEntree = models.DateTimeField(verbose_name="Date et heure du début de l'hebergement")
	DateSortie = models.DateTimeField(verbose_name="Date et heure de la fin de l'hebergement")
	TypeHebergement = models.CharField(max_length=20, verbose_name="Nature de l'hebergement")
	OrientationSortie =  models.CharField(max_length=30, verbose_name="Orientation à la sortie")

	def __unicode__(self):
		return "{0} {{1}} {{2}} {{3}} {{4}} [{5}]".format(self.Hebergement.NumeroPersonne, self.Hebergement.IdCentre, self.Hebergement.DateEntree, self.Hebergement.DateSortie, self.Hebergement.TypeHebergement, self.Hebergement.OrientationSortie)

class Beneficier(models.Model):
	NumeroPersonne = models.ForeignKey('Personne')
	IdService = models.ForeignKey('Service')
	DateService = models.DateTimeField()

	def __unicode__(self):
		return "{0} {{1}} [{2}]".format(self.Beneficier.NumeroPersonne, self.Beneficier.IdService, self.Beneficier.DateService)


### la classe etre est remplacée par la relation de plusieurs à plusieurs entre Personne et Situation matérialisé par IdSituation = models.ManyToManyField('Situation') dans la classe Personne.
class etre(models.Model):
	NumeroPersonne = models.ForeignKey('Personne')
	IdSituation = models.ForeignKey('Situation')
	
	def __unicode__(self):
		return "{0} [{1}]".format(self.etre.NumeroPersonne, self.etre.IdSituation)

	


	
	
	
	

	



	
	
	
	


























