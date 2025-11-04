# custom.py
# command line: scons profile=custom.py build_profile=custom.build

# run this every time after opening terminal
# emsdk_env.bat

# base
platform="web"
target="template_release"
debug_symbols="no"
tools="no"

# https://docs.godotengine.org/en/4.4/contributing/development/compiling/optimizing_for_size.html
lto="full"
optimize="size"
module_text_server_adv_enabled="yes"
module_text_server_fb_enabled="yes"
disable_3d="yes"
disable_advanced_gui="no"

# options
deprecated="no"
minizip="no"
vulkan="no"
use_volk="no"

# Generated using https://godot-build-options-generator.github.io
module_camera_enabled = "no"
module_csg_enabled = "no"
module_dds_enabled = "no"
module_enet_enabled = "no"
module_gltf_enabled = "no"
module_gridmap_enabled = "no"
module_hdr_enabled = "no"
module_jsonrpc_enabled = "no"
module_ktx_enabled = "no"
module_meshoptimizer_enabled = "no"
module_mobile_vr_enabled = "no"
module_multiplayer_enabled = "no"
module_navigation_enabled = "no"
module_noise_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_squish_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"
