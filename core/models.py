from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('descricao',)

    def __str__(self):
        return self.descricao

class Produto (models.Model):
    descricao = models.CharField("Descricao", max_length=150)
    preco = models.DecimalField("Preco", max_digits=9, decimal_places=2)

    quantidade = models.IntegerField("Quantidade")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,
                                  blank=True, null=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ("descricao",)

    def __str__(self):
        return self.descricao


