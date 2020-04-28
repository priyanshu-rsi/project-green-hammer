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

#include "global_deleter.h"
#include "list.h"
#include "object.h"

typedef struct
{
    void *user_data;
    akvcam_deleter_t deleter;
} akvcam_deleters_callback, *akvcam_deleters_callback_t;

typedef akvcam_list_tt(akvcam_deleters_callback_t) akvcam_deleters_list_t;

static akvcam_deleters_list_t akvcam_global_deleter = NULL;

void akvcam_global_deleter_add(void *user_data, akvcam_deleter_t deleter)
{
    akvcam_deleters_callback callback = {user_data, deleter};

    if (!akvcam_global_deleter)
        akvcam_global_deleter = akvcam_list_new();

    akvcam_list_push_back(akvcam_global_deleter,
                         &callback,
                         sizeof(akvcam_deleters_callback),
                         NULL,
                         false);
}

void akvcam_global_deleter_run(void)
{
    akvcam_list_element_t it = NULL;
    akvcam_deleters_callback_t callback;

    if (!akvcam_global_deleter)
        return;

    for (;;) {
        callback = akvcam_list_next(akvcam_global_deleter, &it);

        if (!it)
            break;

        callback->deleter(&callback->user_data);
    }

    akvcam_list_delete(&akvcam_global_deleter);
}
