# UI & Branding

## Runtime

- Drippy Loading Screen controla o boot.
- FancyMenu controla o title screen e estilos globais.
- Default Options aplica padrões a instalações novas.
- O branding resource pack substitui assets vanilla selecionados.

## Asset paths

- config/fancymenu/assets/menu_background.png
- config/fancymenu/assets/cobblehorizons_logo.png
- config/fancymenu/assets/button_normal.png
- config/fancymenu/assets/button_hover.png
- config/fancymenu/assets/button_inactive.png
- config/fancymenu/assets/loading_bar_background.png
- config/fancymenu/assets/loading_bar_progress.png

## Design system

- base escura para legibilidade;
- azul e verde como cores de destaque;
- texto principal branco;
- hover verde claro;
- bordas preservadas por nine-slicing de 8 px;
- wallpapers em 16:9;
- GUI Scale de referência: 3.

## Architecture

O menu principal usa um layout dedicado. As demais telas usam Global Customizations, evitando overrides frágeis de telas complexas. Custom GUIs só devem ser usados quando um fluxo realmente exigir substituição completa.

## Validation

Teste sempre em resoluções diferentes. Nenhum elemento visual pode impedir cliques, leitura, navegação por teclado ou acesso a configurações.