from flask import Blueprint, jsonify
from models import db, AlarmInfo

alarm_bp = Blueprint('alarm_bp', __name__)

@alarm_bp.route('/api/alarms', methods=['GET'])
def get_alarms():
    alarms = AlarmInfo.query.all()
    alarm_list = [{"id": alarm.id, "message": alarm.message, "severity": alarm.severity} for alarm in alarms]
    return jsonify(alarm_list)

