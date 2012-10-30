#!/usr/bin/env python
from article.picture import Picture
from article.avatar import Avatar

pictures_all = [Picture(data=each) for each in Picture.datatype.find()]
avatars_all = [Avatar(data=each) for each in Avatar.datatype.find()]
for each in pictures_all + avatars_all:
    print each.thumb_name, each.file_name
    if len(each.thumb_name.split(ur'/')) > 1:
        each.thumb_name = each.thumb_name.split(ur'/')[-1]
        each.file_name = each.file_name.split(ur'/')[-1]
