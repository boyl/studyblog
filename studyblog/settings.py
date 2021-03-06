"""
Django settings for studyblog project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps目录加入搜索路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1-b7-8kdgaa2#ph95033*@!st8i@9psyohnht!*_2u^y_%og-v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # 添加人性化过滤器
    'django.contrib.sitemaps',  # 网站地图
    'django.contrib.sites',  # allauth需要注册的应用
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',
    'oauth',  # 自定义用户
    'blog',
    'comment',
    'tool',
    'crispy_forms',
    'imagekit',
    'rest_framework',
    'haystack',
]

# 自定义用户model
AUTH_USER_MODEL = 'oauth.Ouser'

# 设置登录和注册成功后重定向的页面，默认是/accounts/profile/
LOGIN_REDIRECT_URL = "/"

SITE_ID = 3

# 禁用注册邮箱验证
ACCOUNT_EMAIL_VERIFICATION = 'none'

# 登录方式，选择用户名或者邮箱都能登录
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# 设置用户注册的时候必须填写邮箱地址
ACCOUNT_EMAIL_REQUIRED = True

# 登出直接退出，不用确认
ACCOUNT_LOGOUT_ON_GET = True

# 表单插件的配置
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studyblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'blog.context_processors.settings_info',  # 自定义上下文管理器
            ],
        },
    },
]

# allauth配置
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'studyblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studyblog',
        'USER': 'root',
        'PASSWORD': 'mysql',
        # 'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 网站默认设置和上下文信息
SITE_END_TITLE = 'TendCode'
SITE_DESCRIPTION = 'description-网站描述'
SITE_KEYWORDS = 'keyword-网站关键词，多个词用英文逗号隔开'

# 统一分页设置
BASE_PAGE_BY = 10
BASE_ORPHANS = 5


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# 邮箱设置
EMAIL_HOST = 'smtp.sina.com'

EMAIL_PORT = 465
EMAIL_USE_SSL = True  # 因465端口，需启用此项
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10  # 对搜索结果分页  已重新定义搜索试图, 不必全局设置.
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

