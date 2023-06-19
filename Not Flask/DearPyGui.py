import dearpygui.dearpygui as dpg
from DearPieConfig import debug

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)


# viewport_width = dpg.get_viewport_client_width()
# viewport_height = dpg.get_viewport_client_height()

# guarantee these commands happen in another frame
# dpg.split_frame()
# width = dpg.get_item_width(modal_id)
# height = dpg.get_item_height(modal_id)
# dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

def dsf():
    dpg.delete_item("window_user")


with dpg.font_registry():
    with dpg.font('static/RobotoMono-VariableFont_wght.ttf', 17, default_font=True, id="Default font"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font("Default font")

width, height, channels, data = dpg.load_image("static/s.webp")

with dpg.texture_registry():
    texture_id = dpg.add_static_texture(width, height, data)


with dpg.window(label="Ачивки", width=800, height=800, pos=(100, 100), tag="window_user"):
    # dpg.add_text("Containers can be nested for advanced layout options")
    # with dpg.child_window(width=500, height=320, menubar=True):
    # with dpg.child_window(autosize_x=True):
    #     dpg.add_text("gdf can be nested for advanced layout options")
    #     dpg.add_text("gfdgfd can be nested for advanced layout options")
    with dpg.child_window(autosize_x=True, height=175):
        with dpg.group(horizontal=True, width=0):
            with dpg.child_window(width=102, height=150):
                dpg.add_image("texture_tag")
            with dpg.child_window(width=300, height=150):
                dpg.add_button(label="Button 1")
                dpg.add_button(label="Button 2")
                dpg.add_button(label="Button 3")
            with dpg.child_window(width=50, height=150):
                dpg.add_button(label="B1", width=25, height=25)
                dpg.add_button(label="B2", width=25, height=25)
                dpg.add_button(label="B3", width=25, height=25)
    with dpg.group(horizontal=True):
        dpg.add_button(label="Footer 1", width=175)
        dpg.add_text("Footer 2")
        dpg.add_button(label="Footer 3", width=175)
dpg.add_button(label="Delete Buttons", callback=dsf, tag="delete_button")

if debug == 2:
    dpg.show_documentation()
    dpg.show_style_editor()
    dpg.show_debug()
    dpg.show_about()
    dpg.show_metrics()
    dpg.show_font_manager()
    dpg.show_item_registry()
elif debug == 1:
    dpg.show_documentation()
    dpg.show_metrics()
    dpg.show_item_registry()
    dpg.show_font_manager()

dpg.setup_dearpygui()
print(23)
dpg.show_viewport()
print(23)
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    dpg.render_dearpygui_frame()
