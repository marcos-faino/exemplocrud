from django.db import models


class Produto (models.Model):
    descricao = models.CharField("Descricao", max_length=150)
    preco = models.DecimalField("Preco", max_digits=9, decimal_places=2)

    quantidade = models.IntegerField("Quantidade")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.descricao


