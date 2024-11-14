from django.template.context_processors import request
from rest_framework import serializers
# from rest_framework.permissions import IsAuthenticated
from lms.models import Course, Lesson
from lms.validators import VideoUrlValidator
from users.models import Subscription
from users.serializers import SubscriptionSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'preview', 'video_url', 'course_id', 'author', 'usd_price')
        validators = [VideoUrlValidator(field="video_url")]


class LessonOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'preview', 'video_url', 'course_id', 'author', 'product_id', 'price_id', 'pay_id', 'usd_price')
        validators = [VideoUrlValidator(field="video_url")]


class CourseSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()


    def get_subscription(self, course):
        return Subscription.objects.filter(course_id=course.id).filter(user=self.context['request'].user).exists()


    class Meta:
        model = Course
        fields = ('id', 'title', 'preview', 'description', 'author', 'subscription', 'product_id', 'usd_price')


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_quantity = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, course):
        return Subscription.objects.filter(course_id=course.id).filter(user=self.context['request'].user).exists()

    def get_lessons_quantity(self, course):
        return Lesson.objects.filter(course_id=course.id).count()


    class Meta:
        model = Course

        fields = ('title', 'preview', 'description', 'lessons_quantity', 'author', 'subscription', 'usd_price', 'lessons')


class CourseDetailOwnerSerializer(CourseDetailSerializer):

    class Meta:
        model = Course

        fields = (
        'title', 'preview', 'description', 'lessons_quantity', 'author', 'subscription', 'product_id', 'price_id', 'pay_id', 'usd_price', 'lessons')

