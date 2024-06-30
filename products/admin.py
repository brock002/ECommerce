from django.contrib import admin
from django.utils.html import format_html
from .models import Product

# Register your models here.
# Registering custom Product ModelAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name", 'description']
    list_display = ["show_product"]

    # Defining how to show Products in the list
    @admin.display(description="Product")
    def show_product(self, obj):
        return format_html(
            """
                <div style="display: flex;">
                    <div><img src="{}" alt="product image" width="100px" style="object-fit: contain;" /></div>
                    <div style="display: flex; flex-direction: column;">
                        <p style="line-height: 100%; font-size: 1rem">{}</p>
                        <p>price: ₹{} / item</p>
                    </div>
                </div>
            """.format(obj.image.url, obj.name, obj.price)
        )