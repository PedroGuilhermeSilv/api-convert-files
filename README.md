# django-ninja

## O padrão utilizado foi o Factory Method
- O `Produto` declara a interface, que é comum a todos os objetos que podem ser produzidos pelo criador e suas subclasses.
- A `classe Criador` declara o método fábrica que retorna novos objetos produto. É importante que o tipo de retorno desse método corresponda à interface do produto. Você pode declarar o método fábrica como abstrato para forçar todas as subclasses a implementar suas próprias versões do método. Como alternativa, o método fábrica base pode retornar algum tipo de produto padrão.

