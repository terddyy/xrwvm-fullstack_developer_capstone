from .models import CarMake, CarModel

def initiate():
    """
    Populate the database with 5 CarMakes and 3 CarModels each
    if the database is empty.
    """
    if CarMake.objects.exists():
        return  # Prevent duplicate population

    # Define 5 car makes
    car_makes = [
        {"name": "Toyota", "description": "Reliable Japanese brand"},
        {"name": "Honda", "description": "Sporty and efficient"},
        {"name": "Ford", "description": "American classic"},
        {"name": "BMW", "description": "Luxury German brand"},
        {"name": "Tesla", "description": "Innovative electric vehicles"},
    ]

    for make_data in car_makes:
        make = CarMake.objects.create(
            name=make_data["name"],
            description=make_data["description"]
        )

        # Add 3 car models for each make
        for i in range(1, 4):
            CarModel.objects.create(
                name=f"{make.name} Model {i}",
                car_make=make,
                type="Sedan" if i % 2 == 0 else "SUV",
                year=2020 + i,
            )
