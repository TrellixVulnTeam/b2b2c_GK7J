# Generated by Django 2.2.1 on 2019-06-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbAddress',
            fields=[
                ('a_id', models.AutoField(db_column='A_id', primary_key=True, serialize=False, verbose_name='ID')),
                ('a_address', models.CharField(db_column='A_address', max_length=50, verbose_name='地址')),
            ],
            options={
                'verbose_name': '收货地址',
                'db_table': 'tb_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbAdmin',
            fields=[
                ('ad_id', models.AutoField(db_column='Ad_id', primary_key=True, serialize=False)),
                ('ad_username', models.CharField(db_column='Ad_username', max_length=20)),
                ('ad_password', models.CharField(db_column='Ad_password', max_length=20)),
                ('ad_nickname', models.CharField(blank=True, db_column='Ad_nickname', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tb_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBuyer',
            fields=[
                ('b_id', models.AutoField(db_column='B_id', primary_key=True, serialize=False, verbose_name='买家ID')),
                ('username', models.CharField(db_column='B_username', max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(db_column='B_password', max_length=20, verbose_name='密码')),
                ('b_phone', models.CharField(blank=True, db_column='B_phone', max_length=15, null=True, verbose_name='手机号')),
                ('b_nickname', models.CharField(blank=True, db_column='B_nickname', max_length=20, null=True, verbose_name='昵称')),
                ('b_createtime', models.DateTimeField(db_column='B_createtime', verbose_name='注册时间')),
                ('b_headportrait', models.CharField(blank=True, db_column='B_headportrait', max_length=50, null=True, verbose_name='买家头像相对路径')),
                ('b_intro', models.CharField(blank=True, db_column='B_intro', max_length=500, null=True, verbose_name='买家简介')),
                ('b_taken', models.CharField(db_column='B_taken', max_length=200, null=True, verbose_name='登录taken')),
            ],
            options={
                'verbose_name': '买家表',
                'db_table': 'tb_buyer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCategory',
            fields=[
                ('c_id', models.IntegerField(db_column='C_id', primary_key=True, serialize=False, verbose_name='分类ID')),
                ('c_name', models.CharField(db_column='C_name', max_length=20, verbose_name='分类名称')),
                ('c_desc', models.CharField(blank=True, db_column='C_desc', max_length=100, null=True, verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '分类表',
                'db_table': 'tb_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbLogistics',
            fields=[
                ('l_id', models.AutoField(db_column='L_id', primary_key=True, serialize=False, verbose_name='物流信息ID')),
                ('l_start', models.CharField(db_column='L_start', max_length=50, verbose_name='发货地址')),
                ('l_current', models.CharField(db_column='L_current', max_length=50, verbose_name='当前位置')),
                ('l_end', models.CharField(db_column='L_end', max_length=50, verbose_name='收货地址')),
                ('o_id', models.IntegerField(db_column='O_id', verbose_name='订单ID')),
            ],
            options={
                'verbose_name': '物流信息表',
                'db_table': 'tb_logistics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbOrders',
            fields=[
                ('o_id', models.AutoField(db_column='O_id', primary_key=True, serialize=False, verbose_name='订单ID')),
                ('o_bname', models.CharField(db_column='O_bname', max_length=20, verbose_name='收货人姓名')),
                ('o_bphone', models.CharField(db_column='O_bphone', max_length=15, verbose_name='收货人电话')),
                ('o_time', models.DateTimeField(db_column='O_time', verbose_name='订单生成时间')),
                ('o_address', models.CharField(db_column='O_address', max_length=100, verbose_name='收货地址')),
                ('o_state', models.IntegerField(db_column='O_state', verbose_name='订单状态 ')),
                ('o_total', models.FloatField(blank=True, db_column='O_total', null=True, verbose_name='订单总价')),
            ],
            options={
                'verbose_name': '订单表',
                'db_table': 'tb_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbOrdersitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oi_count', models.IntegerField(db_column='OI_count', verbose_name='商品数量')),
                ('oi_sum', models.FloatField(db_column='OI_sum', verbose_name='小计金额')),
            ],
            options={
                'verbose_name': '订单项表',
                'db_table': 'tb_ordersitem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbProduct',
            fields=[
                ('p_id', models.AutoField(db_column='P_id', primary_key=True, serialize=False, verbose_name='商品ID')),
                ('p_name', models.CharField(db_column='P_name', max_length=50, verbose_name='商品名')),
                ('p_price', models.FloatField(db_column='P_price', verbose_name='商品单价')),
                ('p_uptime', models.DateTimeField(db_column='P_uptime', verbose_name='商品上架时间')),
                ('p_image', models.CharField(db_column='P_image', max_length=50, verbose_name='商品图片相对路径地址')),
                ('p_desc', models.CharField(blank=True, db_column='P_desc', max_length=500, null=True, verbose_name='商品描述')),
                ('p_inventory', models.IntegerField(blank=True, db_column='P_inventory', null=True, verbose_name='商品库存量')),
            ],
            options={
                'verbose_name': '商品表',
                'db_table': 'tb_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbProductcar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_state', models.IntegerField(blank=True, db_column='Pc_state', null=True, verbose_name='交易状态')),
                ('pc_count', models.IntegerField(blank=True, db_column='Pc_count', null=True, verbose_name='商品数量')),
            ],
            options={
                'verbose_name': '购物车商品表',
                'db_table': 'tb_productcar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbSeller',
            fields=[
                ('s_id', models.AutoField(db_column='S_id', primary_key=True, serialize=False, verbose_name='卖家ID')),
                ('s_username', models.CharField(db_column='S_username', max_length=20, unique=True, verbose_name='用户名')),
                ('s_password', models.CharField(db_column='S_password', max_length=20, verbose_name='密码')),
                ('s_phone', models.CharField(blank=True, db_column='S_phone', max_length=15, null=True, verbose_name='手机号')),
                ('s_nickname', models.CharField(blank=True, db_column='S_nickname', max_length=20, null=True, verbose_name='昵称')),
                ('s_createtime', models.DateTimeField(db_column='S_createtime', verbose_name='注册时间')),
                ('s_headportrait', models.CharField(blank=True, db_column='S_headportrait', max_length=50, null=True, verbose_name='卖家头像相对路径')),
                ('s_intro', models.CharField(blank=True, db_column='S_intro', max_length=500, null=True, verbose_name='卖家简介')),
            ],
            options={
                'verbose_name': '卖家个人信息表 ',
                'db_table': 'tb_seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbShopcar',
            fields=[
                ('sc_id', models.AutoField(db_column='Sc_id', primary_key=True, serialize=False, verbose_name='购物车ID')),
                ('b_no', models.IntegerField(db_column='B_no', unique=True, verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '购物车表',
                'db_table': 'tb_shopcar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbStore',
            fields=[
                ('st_id', models.AutoField(db_column='St_id', primary_key=True, serialize=False, verbose_name='店铺ID')),
                ('st_name', models.CharField(db_column='St_name', max_length=20, unique=True, verbose_name='店铺名称')),
                ('st_desc', models.CharField(blank=True, db_column='St_desc', max_length=500, null=True, verbose_name='店铺描述')),
                ('s_id', models.IntegerField(db_column='S_id', verbose_name='卖家ID')),
            ],
            options={
                'verbose_name': '店铺表',
                'db_table': 'tb_store',
                'managed': False,
            },
        ),
    ]
