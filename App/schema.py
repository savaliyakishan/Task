import graphene
from graphene_django import DjangoObjectType
from .models import City


class CityType(DjangoObjectType):
    class Meta:
        model = City
        fields = ('id','city')

class CreateCity(graphene.Mutation):
   
    class Arguments:
        city= graphene.String()   
        
    city = graphene.Field(CityType)

    @classmethod
    def mutate(cls, root, info, **city_data):
        obj = City(
            city=city_data.get('city')
        )
        
        obj.save()
        return CreateCity(city=obj)

class UpdateCity(graphene.Mutation):
        class Arguments:
            id = graphene.ID()
            city = graphene.String()
            


        city = graphene.Field(CityType)

        @classmethod
        def mutate(cls, root, info, id, **update_data):
            city = City.objects.filter(id=id)
            if city:
                city.update(city = update_data['city'])
                return UpdateCity(city=city.first())
            else:
                print('User with given ID does not exist.')

class DeleteUser(graphene.Mutation):
        class Arguments:
            id = graphene.ID()

        city = graphene.Field(CityType)

        @classmethod
        def mutate(cls, root, info, id):
            city = City.objects.get(id=id)
            city.delete()
            return DeleteUser(city)


class Query(graphene.ObjectType):
    all_city = graphene.List(CityType)
    city_by_id = graphene.Field(CityType, id=graphene.String())

    def resolve_all_city(root, info):
        return City.objects.all().order_by('id')
    
    def resolve_city_by_id(root, info,id):
            return City.objects.get(id=id)
    

class Mutation(graphene.ObjectType):
    create_city = CreateCity.Field()
    update_city = UpdateCity.Field()
    delete_city = DeleteUser.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)
