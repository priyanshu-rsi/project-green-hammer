/* akvcam, virtual camera for Linux.
 * Copyright (C) 2018  Gonzalo Exequiel Pedone
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#ifndef AKVCAM_DEVICE_H
#define AKVCAM_DEVICE_H

#include <linux/videodev2.h>

#include "device_types.h"
#include "buffers_types.h"
#include "controls_types.h"
#include "format_types.h"
#include "node_types.h"

struct file;

// public
akvcam_device_t akvcam_device_new(const char *name,
                                  const char *description,
                                  AKVCAM_DEVICE_TYPE type,
                                  AKVCAM_RW_MODE rw_mode,
                                  bool multiplanar);
void akvcam_device_delete(akvcam_device_t *self);

bool akvcam_device_register(akvcam_device_t self);
void akvcam_device_unregister(akvcam_device_t self);
u16 akvcam_device_num(const akvcam_device_t self);
const char *akvcam_device_description(const akvcam_device_t self);
AKVCAM_DEVICE_TYPE akvcam_device_type(const akvcam_device_t self);
enum v4l2_buf_type akvcam_device_v4l2_type(const akvcam_device_t self);
AKVCAM_RW_MODE akvcam_device_rw_mode(const akvcam_device_t self);
akvcam_formats_list_t akvcam_device_formats_nr(const akvcam_device_t self);
akvcam_formats_list_t akvcam_device_formats(const akvcam_device_t self);
akvcam_format_t akvcam_device_format_nr(const akvcam_device_t self);
akvcam_format_t akvcam_device_format(const akvcam_device_t self);
akvcam_controls_t akvcam_device_controls_nr(const akvcam_device_t self);
akvcam_controls_t akvcam_device_controls(const akvcam_device_t self);
akvcam_nodes_list_t akvcam_device_nodes_nr(const akvcam_device_t self);
akvcam_nodes_list_t akvcam_device_nodes(const akvcam_device_t self);
akvcam_buffers_t akvcam_device_buffers_nr(const akvcam_device_t self);
akvcam_buffers_t akvcam_device_buffers(const akvcam_device_t self);
enum v4l2_priority akvcam_device_priority(const akvcam_device_t self);
akvcam_node_t akvcam_device_priority_node(const akvcam_device_t self);
void akvcam_device_set_priority(akvcam_device_t self,
                                enum v4l2_priority priority,
                                akvcam_node_t node);
enum v4l2_priority akvcam_device_priority(const akvcam_device_t self);
bool akvcam_device_streaming(const akvcam_device_t self);
bool akvcam_device_streaming_rw(const akvcam_device_t self);
void akvcam_device_set_streaming(akvcam_device_t self, bool streaming);
void akvcam_device_set_streaming_rw(akvcam_device_t self, bool streaming);
bool akvcam_device_prepare_frame(akvcam_device_t self);
akvcam_devices_list_t akvcam_device_connected_devices_nr(const akvcam_device_t self);
akvcam_devices_list_t akvcam_device_connected_devices(const akvcam_device_t self);
bool akvcam_device_multiplanar(const akvcam_device_t self);
void akvcam_device_set_multiplanar(akvcam_device_t self, bool multiplanar);
__u32 akvcam_device_caps(const akvcam_device_t self);

// public static
size_t akvcam_device_sizeof(void);
akvcam_device_t akvcam_device_from_file_nr(struct file *filp);
akvcam_device_t akvcam_device_from_file(struct file *filp);

#endif //AKVCAM_ DEVICE_H
