# Generated by Django 3.2.6 on 2021-08-27 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import guacamole.fields

print(settings.DATABASES)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuacamoleConnection',
            fields=[
                ('connection_id', models.AutoField(primary_key=True, serialize=False)),
                ('connection_name', models.CharField(max_length=128)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('protocol', models.CharField(default='rdp', max_length=32)),
                ('proxy_port', models.IntegerField(blank=True, null=True)),
                ('proxy_hostname', models.CharField(blank=True, max_length=512, null=True)),
                ('proxy_encryption_method', models.CharField(blank=True, max_length=4, null=True)),
                ('max_connections', models.IntegerField(blank=True, null=True)),
                ('max_connections_per_user', models.IntegerField(blank=True, null=True)),
                ('connection_weight', models.IntegerField(blank=True, null=True)),
                ('failover_only', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'guacamole_connection',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionGroup',
            fields=[
                ('connection_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('connection_group_name', models.CharField(max_length=128)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('type', guacamole.fields.GuacamoleConnectionGroupTypeField(choices=[('ORGANIZATIONAL', 'ORGANIZATIONAL'), ('BALANCING', 'BALANCING')], default='ORGANIZATIONAL')),
                ('max_connections', models.IntegerField(blank=True, null=True)),
                ('max_connections_per_user', models.IntegerField(blank=True, null=True)),
                ('enable_session_affinity', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'guacamole_connection_group',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('remote_host', models.CharField(blank=True, max_length=256, null=True)),
                ('connection_name', models.CharField(max_length=128)),
                ('sharing_profile_name', models.CharField(blank=True, max_length=128, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'guacamole_connection_history',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleEntity',
            fields=[
                ('entity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'guacamole_entity',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleSharingProfile',
            fields=[
                ('sharing_profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('sharing_profile_name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'guacamole_sharing_profile',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=32)),
                ('password_salt', models.CharField(blank=True, max_length=32, null=True)),
                ('password_date', models.DateTimeField(auto_now_add=True)),
                ('disabled', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
                ('access_window_start', models.TimeField(blank=True, null=True)),
                ('access_window_end', models.TimeField(blank=True, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=64, null=True)),
                ('full_name', models.CharField(blank=True, max_length=256, null=True)),
                ('email_address', models.CharField(blank=True, max_length=256, null=True)),
                ('organization', models.CharField(blank=True, max_length=256, null=True)),
                ('organizational_role', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'guacamole_user',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserGroup',
            fields=[
                ('user_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('disabled', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'guacamole_user_group',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('remote_host', models.CharField(blank=True, max_length=256, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'guacamole_user_history',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserPasswordHistory',
            fields=[
                ('password_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=32)),
                ('password_salt', models.CharField(blank=True, max_length=32, null=True)),
                ('password_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'guacamole_user_password_history',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionAttribute',
            fields=[
                ('connection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleconnection')),
                ('attribute_name', models.CharField(max_length=128)),
                ('attribute_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_connection_attribute',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionGroupAttribute',
            fields=[
                ('connection_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleconnectiongroup')),
                ('attribute_name', models.CharField(max_length=128)),
                ('attribute_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_connection_group_attribute',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionGroupPermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleObjectPermissionTypeField(choices=[('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'), ('ADMINISTER', 'ADMINISTER')], default='READ')),
            ],
            options={
                'db_table': 'guacamole_connection_group_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionParameter',
            fields=[
                ('connection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleconnection')),
                ('parameter_name', models.CharField(max_length=128)),
                ('parameter_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_connection_parameter',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleConnectionPermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleObjectPermissionTypeField(choices=[('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'), ('ADMINISTER', 'ADMINISTER')], default='READ')),
            ],
            options={
                'db_table': 'guacamole_connection_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleSharingProfileAttribute',
            fields=[
                ('sharing_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamolesharingprofile')),
                ('attribute_name', models.CharField(max_length=128)),
                ('attribute_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_sharing_profile_attribute',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleSharingProfileParameter',
            fields=[
                ('sharing_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamolesharingprofile')),
                ('parameter_name', models.CharField(max_length=128)),
                ('parameter_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_sharing_profile_parameter',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleSharingProfilePermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleObjectPermissionTypeField(choices=[('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'), ('ADMINISTER', 'ADMINISTER')], default='READ')),
            ],
            options={
                'db_table': 'guacamole_sharing_profile_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleSystemPermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleSystemPermissionTypeField(choices=[('CREATE_CONNECTION', 'CREATE_CONNECTION'), ('CREATE_CONNECTION_GROUP', 'CREATE_CONNECTION_GROUP'), ('CREATE_USER', 'CREATE_USER'), ('ADMINISTER', 'ADMINISTER')])),
            ],
            options={
                'db_table': 'guacamole_system_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserAttribute',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleuser')),
                ('attribute_name', models.CharField(max_length=128)),
                ('attribute_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_user_attribute',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserGroupAttribute',
            fields=[
                ('user_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleusergroup')),
                ('attribute_name', models.CharField(max_length=128)),
                ('attribute_value', models.CharField(max_length=4096)),
            ],
            options={
                'db_table': 'guacamole_user_group_attribute',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserGroupMember',
            fields=[
                ('user_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleusergroup')),
            ],
            options={
                'db_table': 'guacamole_user_group_member',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserGroupPermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleObjectPermissionTypeField(choices=[('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'), ('ADMINISTER', 'ADMINISTER')], default='READ')),
            ],
            options={
                'db_table': 'guacamole_user_group_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
        migrations.CreateModel(
            name='GuacamoleUserPermission',
            fields=[
                ('entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guacamole.guacamoleentity')),
                ('permission', guacamole.fields.GuacamoleObjectPermissionTypeField(choices=[('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'), ('ADMINISTER', 'ADMINISTER')], default='READ')),
            ],
            options={
                'db_table': 'guacamole_user_permission',
                'managed': settings.RUNNING_TESTS,
            },
        ),
    ]

    if not settings.RUNNING_TESTS:
        operations.append(
            migrations.RunSQL("""
CREATE TABLE `guacamole_connection_group` (

  `connection_group_id`   int(11)      NOT NULL AUTO_INCREMENT,
  `parent_id`             int(11),
  `connection_group_name` varchar(128) NOT NULL,
  `type`                  enum('ORGANIZATIONAL',
                               'BALANCING') NOT NULL DEFAULT 'ORGANIZATIONAL',

  `max_connections`          int(11),
  `max_connections_per_user` int(11),
  `enable_session_affinity`  boolean NOT NULL DEFAULT 0,

  PRIMARY KEY (`connection_group_id`),
  UNIQUE KEY `connection_group_name_parent` (`connection_group_name`, `parent_id`),

  CONSTRAINT `guacamole_connection_group_ibfk_1`
    FOREIGN KEY (`parent_id`)
    REFERENCES `guacamole_connection_group` (`connection_group_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_connection` (

  `connection_id`       int(11)      NOT NULL AUTO_INCREMENT,
  `connection_name`     varchar(128) NOT NULL,
  `parent_id`           int(11),
  `protocol`            varchar(32)  NOT NULL,
  `proxy_port`              integer,
  `proxy_hostname`          varchar(512),
  `proxy_encryption_method` enum('NONE', 'SSL'),
  `max_connections`          int(11),
  `max_connections_per_user` int(11),
  `connection_weight`        int(11),
  `failover_only`            boolean NOT NULL DEFAULT 0,

  PRIMARY KEY (`connection_id`),
  UNIQUE KEY `connection_name_parent` (`connection_name`, `parent_id`),

  CONSTRAINT `guacamole_connection_ibfk_1`
    FOREIGN KEY (`parent_id`)
    REFERENCES `guacamole_connection_group` (`connection_group_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_entity` (

  `entity_id`     int(11)            NOT NULL AUTO_INCREMENT,
  `name`          varchar(128)       NOT NULL,
  `type`          enum('USER',
                       'USER_GROUP') NOT NULL,

  PRIMARY KEY (`entity_id`),
  UNIQUE KEY `guacamole_entity_name_scope` (`type`, `name`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_user` (

  `user_id`       int(11)      NOT NULL AUTO_INCREMENT,
  `entity_id`     int(11)      NOT NULL,

  `password_hash` binary(32)   NOT NULL,
  `password_salt` binary(32),
  `password_date` datetime     NOT NULL,

  `disabled`      boolean      NOT NULL DEFAULT 0,
  `expired`       boolean      NOT NULL DEFAULT 0,

  `access_window_start`    TIME,
  `access_window_end`      TIME,

  `valid_from`  DATE,
  `valid_until` DATE,

  `timezone` VARCHAR(64),

  `full_name`           VARCHAR(256),
  `email_address`       VARCHAR(256),
  `organization`        VARCHAR(256),
  `organizational_role` VARCHAR(256),

  PRIMARY KEY (`user_id`),

  UNIQUE KEY `guacamole_user_single_entity` (`entity_id`),

  CONSTRAINT `guacamole_user_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_user_group` (

  `user_group_id` int(11)      NOT NULL AUTO_INCREMENT,
  `entity_id`     int(11)      NOT NULL,

  `disabled`      boolean      NOT NULL DEFAULT 0,

  PRIMARY KEY (`user_group_id`),

  UNIQUE KEY `guacamole_user_group_single_entity` (`entity_id`),

  CONSTRAINT `guacamole_user_group_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_user_group_member` (

  `user_group_id`    int(11)     NOT NULL,
  `member_entity_id` int(11)     NOT NULL,

  PRIMARY KEY (`user_group_id`, `member_entity_id`),

  CONSTRAINT `guacamole_user_group_member_parent_id`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `guacamole_user_group` (`user_group_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_user_group_member_entity_id`
    FOREIGN KEY (`member_entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_sharing_profile (

  `sharing_profile_id`    int(11)      NOT NULL AUTO_INCREMENT,
  `sharing_profile_name`  varchar(128) NOT NULL,
  `primary_connection_id` int(11)      NOT NULL,

  PRIMARY KEY (`sharing_profile_id`),
  UNIQUE KEY `sharing_profile_name_primary` (sharing_profile_name, primary_connection_id),

  CONSTRAINT `guacamole_sharing_profile_ibfk_1`
    FOREIGN KEY (`primary_connection_id`)
    REFERENCES `guacamole_connection` (`connection_id`)
    ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_connection_parameter` (

  `connection_id`   int(11)       NOT NULL,
  `parameter_name`  varchar(128)  NOT NULL,
  `parameter_value` varchar(4096) NOT NULL,

  PRIMARY KEY (`connection_id`,`parameter_name`),

  CONSTRAINT `guacamole_connection_parameter_ibfk_1`
    FOREIGN KEY (`connection_id`)
    REFERENCES `guacamole_connection` (`connection_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_sharing_profile_parameter (

  `sharing_profile_id` integer       NOT NULL,
  `parameter_name`     varchar(128)  NOT NULL,
  `parameter_value`    varchar(4096) NOT NULL,

  PRIMARY KEY (`sharing_profile_id`, `parameter_name`),

  CONSTRAINT `guacamole_sharing_profile_parameter_ibfk_1`
    FOREIGN KEY (`sharing_profile_id`)
    REFERENCES `guacamole_sharing_profile` (`sharing_profile_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_user_attribute (

  `user_id`         int(11)       NOT NULL,
  `attribute_name`  varchar(128)  NOT NULL,
  `attribute_value` varchar(4096) NOT NULL,

  PRIMARY KEY (user_id, attribute_name),
  KEY `user_id` (`user_id`),

  CONSTRAINT guacamole_user_attribute_ibfk_1
    FOREIGN KEY (user_id)
    REFERENCES guacamole_user (user_id) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_user_group_attribute (

  `user_group_id`   int(11)       NOT NULL,
  `attribute_name`  varchar(128)  NOT NULL,
  `attribute_value` varchar(4096) NOT NULL,

  PRIMARY KEY (`user_group_id`, `attribute_name`),
  KEY `user_group_id` (`user_group_id`),

  CONSTRAINT `guacamole_user_group_attribute_ibfk_1`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `guacamole_user_group` (`user_group_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_connection_attribute (

  `connection_id`   int(11)       NOT NULL,
  `attribute_name`  varchar(128)  NOT NULL,
  `attribute_value` varchar(4096) NOT NULL,

  PRIMARY KEY (connection_id, attribute_name),
  KEY `connection_id` (`connection_id`),

  CONSTRAINT guacamole_connection_attribute_ibfk_1
    FOREIGN KEY (connection_id)
    REFERENCES guacamole_connection (connection_id) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_connection_group_attribute (

  `connection_group_id` int(11)       NOT NULL,
  `attribute_name`      varchar(128)  NOT NULL,
  `attribute_value`     varchar(4096) NOT NULL,

  PRIMARY KEY (connection_group_id, attribute_name),
  KEY `connection_group_id` (`connection_group_id`),

  CONSTRAINT guacamole_connection_group_attribute_ibfk_1
    FOREIGN KEY (connection_group_id)
    REFERENCES guacamole_connection_group (connection_group_id) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_sharing_profile_attribute (

  `sharing_profile_id` int(11)       NOT NULL,
  `attribute_name`     varchar(128)  NOT NULL,
  `attribute_value`    varchar(4096) NOT NULL,

  PRIMARY KEY (sharing_profile_id, attribute_name),
  KEY `sharing_profile_id` (`sharing_profile_id`),

  CONSTRAINT guacamole_sharing_profile_attribute_ibfk_1
    FOREIGN KEY (sharing_profile_id)
    REFERENCES guacamole_sharing_profile (sharing_profile_id) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_connection_permission` (

  `entity_id`     int(11) NOT NULL,
  `connection_id` int(11) NOT NULL,
  `permission`    enum('READ',
                       'UPDATE',
                       'DELETE',
                       'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`,`connection_id`,`permission`),

  CONSTRAINT `guacamole_connection_permission_ibfk_1`
    FOREIGN KEY (`connection_id`)
    REFERENCES `guacamole_connection` (`connection_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_connection_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_connection_group_permission` (

  `entity_id`           int(11) NOT NULL,
  `connection_group_id` int(11) NOT NULL,
  `permission`          enum('READ',
                             'UPDATE',
                             'DELETE',
                             'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`,`connection_group_id`,`permission`),

  CONSTRAINT `guacamole_connection_group_permission_ibfk_1`
    FOREIGN KEY (`connection_group_id`)
    REFERENCES `guacamole_connection_group` (`connection_group_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_connection_group_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_sharing_profile_permission (

  `entity_id`          integer NOT NULL,
  `sharing_profile_id` integer NOT NULL,
  `permission`         enum('READ',
                            'UPDATE',
                            'DELETE',
                            'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`, `sharing_profile_id`, `permission`),

  CONSTRAINT `guacamole_sharing_profile_permission_ibfk_1`
    FOREIGN KEY (`sharing_profile_id`)
    REFERENCES `guacamole_sharing_profile` (`sharing_profile_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_sharing_profile_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_system_permission` (

  `entity_id`  int(11) NOT NULL,
  `permission` enum('CREATE_CONNECTION',
                    'CREATE_CONNECTION_GROUP',
                    'CREATE_SHARING_PROFILE',
                    'CREATE_USER',
                    'CREATE_USER_GROUP',
                    'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`,`permission`),

  CONSTRAINT `guacamole_system_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_user_permission` (

  `entity_id`        int(11) NOT NULL,
  `affected_user_id` int(11) NOT NULL,
  `permission`       enum('READ',
                          'UPDATE',
                          'DELETE',
                          'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`,`affected_user_id`,`permission`),

  CONSTRAINT `guacamole_user_permission_ibfk_1`
    FOREIGN KEY (`affected_user_id`)
    REFERENCES `guacamole_user` (`user_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_user_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_user_group_permission` (

  `entity_id`              int(11) NOT NULL,
  `affected_user_group_id` int(11) NOT NULL,
  `permission`             enum('READ',
                                'UPDATE',
                                'DELETE',
                                'ADMINISTER') NOT NULL,

  PRIMARY KEY (`entity_id`, `affected_user_group_id`, `permission`),

  CONSTRAINT `guacamole_user_group_permission_affected_user_group`
    FOREIGN KEY (`affected_user_group_id`)
    REFERENCES `guacamole_user_group` (`user_group_id`) ON DELETE CASCADE,

  CONSTRAINT `guacamole_user_group_permission_entity`
    FOREIGN KEY (`entity_id`)
    REFERENCES `guacamole_entity` (`entity_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `guacamole_connection_history` (

  `history_id`           int(11)      NOT NULL AUTO_INCREMENT,
  `user_id`              int(11)      DEFAULT NULL,
  `username`             varchar(128) NOT NULL,
  `remote_host`          varchar(256) DEFAULT NULL,
  `connection_id`        int(11)      DEFAULT NULL,
  `connection_name`      varchar(128) NOT NULL,
  `sharing_profile_id`   int(11)      DEFAULT NULL,
  `sharing_profile_name` varchar(128) DEFAULT NULL,
  `start_date`           datetime     NOT NULL,
  `end_date`             datetime     DEFAULT NULL,

  PRIMARY KEY (`history_id`),
  KEY `user_id` (`user_id`),
  KEY `connection_id` (`connection_id`),
  KEY `sharing_profile_id` (`sharing_profile_id`),
  KEY `start_date` (`start_date`),
  KEY `end_date` (`end_date`),
  KEY `connection_start_date` (`connection_id`, `start_date`),

  CONSTRAINT `guacamole_connection_history_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `guacamole_user` (`user_id`) ON DELETE SET NULL,

  CONSTRAINT `guacamole_connection_history_ibfk_2`
    FOREIGN KEY (`connection_id`)
    REFERENCES `guacamole_connection` (`connection_id`) ON DELETE SET NULL,

  CONSTRAINT `guacamole_connection_history_ibfk_3`
    FOREIGN KEY (`sharing_profile_id`)
    REFERENCES `guacamole_sharing_profile` (`sharing_profile_id`) ON DELETE SET NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_user_history (

  `history_id`           int(11)      NOT NULL AUTO_INCREMENT,
  `user_id`              int(11)      DEFAULT NULL,
  `username`             varchar(128) NOT NULL,
  `remote_host`          varchar(256) DEFAULT NULL,
  `start_date`           datetime     NOT NULL,
  `end_date`             datetime     DEFAULT NULL,

  PRIMARY KEY (history_id),
  KEY `user_id` (`user_id`),
  KEY `start_date` (`start_date`),
  KEY `end_date` (`end_date`),
  KEY `user_start_date` (`user_id`, `start_date`),

  CONSTRAINT guacamole_user_history_ibfk_1
    FOREIGN KEY (user_id)
    REFERENCES guacamole_user (user_id) ON DELETE SET NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE guacamole_user_password_history (

  `password_history_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id`             int(11) NOT NULL,

  `password_hash` binary(32) NOT NULL,
  `password_salt` binary(32),
  `password_date` datetime   NOT NULL,

  PRIMARY KEY (`password_history_id`),
  KEY `user_id` (`user_id`),

  CONSTRAINT `guacamole_user_password_history_ibfk_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `guacamole_user` (`user_id`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""))



